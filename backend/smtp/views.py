from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.contrib.auth.models import User
from django.contrib import messages 
from backend.registradores.models import Estatus_Mail, Estatus_PC, Estatus_Web, ZipFile
from backend.plantillas.models import Plantillas
from backend.correos.models import Correos
from backend.smtp.models import Enviados
import os
import random
import string
import shutil
import tempfile

@login_required(login_url='/accounts/login/')
def auditar(request):

    if request.POST['enviar'] == 'enviar':

        usuario = User.get_username(request.user)

        usuario = User.objects.get(username=usuario)
        correo = Correos.objects.get(id=request.POST['id'], propietario=usuario)
        plantilla = Plantillas.objects.get(id=request.POST['plantilla'])

        enviado = Enviados.objects.create(
            plantilla=plantilla,
            correo=correo,
            propietario=usuario
        )

        # 1689d75e-0a56-463b-aaa1-4c741bdb26d5.clouding.host
        link_mail = 'http://192.168.21.130:8000/logo/'+ str(enviado.id)
        link_web = 'http://192.168.21.130:8000/ruta/' + str(enviado.id)



        try: 
            asunto = plantilla.asunto
            contenido = plantilla.mensaje
            emisor = plantilla.emisor
            enviar(emisor, correo.correo, asunto, contenido, link_mail, link_web)
            Estatus_Mail.objects.create(enviado=enviado)
            Estatus_Web.objects.create(enviado=enviado)
            Estatus_PC.objects.create(enviado=enviado)
            enviado.estatus = True
            enviado.save()
            messages.add_message(request, messages.SUCCESS, 'Correo enviado correctamente')
        except:
            messages.add_message(request, messages.ERROR, 'No se ha podido enviar el email')


    else:
        messages.add_message(request, messages.ERROR, 'Introduce correctamente "enviar"')

    return redirect('correos', correo.grupo.id)


def enviar(emisor, destino, asunto, contenido, link_mail, link_web):
    mail_origen = emisor.correo
    password = emisor.contraseña
    mail_destino = destino

    contenido_mensaje = MIMEMultipart()
    contenido_mensaje['From'] = mail_origen
    contenido_mensaje['To'] = mail_destino
    contenido_mensaje['Subject'] = asunto

    contenido = contenido.replace("[mail.link]", link_mail)
    contenido = contenido.replace("[web.link]", link_web)

    contenido_mensaje.attach(MIMEText(contenido,"html"))
    email_string = contenido_mensaje.as_string()
    s = smtplib.SMTP(str(emisor.smtp),int(emisor.puerto))
    s.starttls()
    s.login(mail_origen, password)
    s.sendmail(mail_origen, mail_destino, email_string)
    s.quit()

    return



def generate_random_filename(length=7):
    """Genera un nombre aleatorio alfanumérico de la longitud especificada."""
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def move_compressed_file(filename, target_directory):
    """Mueve un archivo comprimido a un directorio de destino."""
    source_path = os.path.abspath(filename)
    destination_path = os.path.join(target_directory, filename)
    shutil.move(source_path, destination_path)

def save_zip_filename(filename, enviado):
    """Guarda el nombre del archivo en la base de datos de Zip junto con la relación al objeto 'enviado'."""
    zip_file = ZipFile(name=filename, enviado=enviado)
    zip_file.save()


def transform_script_to_exe(plantilla, enviado, ruta):

    # Crea una carpeta temporal para almacenar los archivos generados por PyInstaller
    temp_dir = tempfile.mkdtemp()

    # Crea un archivo temporal para almacenar la plantilla de script
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w')
    temp_file.write(plantilla.script)
    temp_file.close()

    # Lee el contenido del archivo de script original
    with open(temp_file.name, 'r') as f:
        script_content = f.read()

    # Modifica el contenido del script reemplazando '[web.url]' con la ruta proporcionada
    modified_script_content = script_content.replace('[web.url]', ruta)

    # Crea un nuevo archivo temporal con el script modificado
    modified_temp_file = tempfile.NamedTemporaryFile(delete=False)
    modified_temp_file.write(modified_script_content.encode())
    modified_temp_file.close()

    # Establece la carpeta de destino para la distribución del ejecutable
    dist_path = os.path.join(temp_dir, 'dist')
    os.makedirs(dist_path)  # Crea la carpeta dist

    # Construye el comando de PyInstaller para convertir el script en un ejecutable
    nombre_archivo = generate_random_filename()  # Genera un nombre aleatorio para el archivo ejecutable
    comando = f'pyinstaller --onefile --noconsole --icon={plantilla.icono.path} --specpath={temp_dir} --distpath={dist_path} --name={nombre_archivo}.exe --win-private-assemblies {modified_temp_file.name}'
    os.system(comando)


    # Obtiene la ruta del archivo .exe generado por PyInstaller
    exe_filename = os.path.join(dist_path, nombre_archivo + '.exe')
    exe_path = os.path.abspath(exe_filename)
    print(exe_path)
    print(exe_filename)

    # Genera un nombre aleatorio para el archivo comprimido
    nombre_comprimido = generate_random_filename() + ".7z"  # Reemplaza 'generate_random_filename()' con tu lógica para generar un nombre aleatorio

    # Construye el comando para empaquetar el archivo ejecutable en un archivo comprimido
    comando2 = f'python3 PackMyPayload/PackMyPayload.py {exe_path} {nombre_comprimido}'
    os.system(comando2)

    # Mueve el archivo comprimido resultante a la carpeta "templates/media/zips"
    target_directory = "templates/media/zips"  # Reemplaza con la ruta correcta
    move_compressed_file(nombre_comprimido, target_directory)  # Reemplaza 'move_compressed_file()' con la lógica para mover el archivo

    # Guarda el nombre del archivo en la base de datos de Zip
    save_zip_filename(nombre_comprimido, enviado)  # Reemplaza 'save_zip_filename()' con la lógica para guardar el nombre en la base de datos
