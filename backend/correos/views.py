from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages 
from backend.grupos.models import Grupos
from backend.smtp.models import Enviados
from backend.correos.models import Correos
from backend.plantillas.models import Plantillas
from backend.registradores.models import Estatus_Mail, Estatus_PC, Estatus_Web, Data

@login_required(login_url='/accounts/login/')
def index(request, id=None):
    if request.method == 'GET':
        datos = obtener_datos_correos(request, id)
        data = {
            'datos': datos,
            'grupo': id
        }
    elif request.method == 'POST':
        # Eliminar correo
        if request.POST['instruccion'] == 'eliminar-correo':
            eliminar_correo(request)
        elif request.POST['instruccion'] == 'cambiar-correo':
            cambiar_correo_grupo(request)
        elif request.POST['instruccion'] == 'añadir-correo':
            añadir_correo(request)
        elif request.POST['instruccion'] == 'eliminar-registro':
            eliminar_registro(request)
        else:
            print('ninguna selección es correcta')
            messages.add_message(request, messages.ERROR, 'Error en la petición')
        
        datos = obtener_datos_correos(request, id)
        data = {
            'datos': datos,
        }
    else:
        print('NO ES UN GET NI UN POST')
        datos = obtener_datos_correos(request, id)
        messages.add_message(request, messages.ERROR, 'Error en la petición')
        data = {
            'datos': datos,
        }
    
    return render(request, 'backend/correos/index.html', data)



# Funcion obtener datos correos

from datetime import datetime

@login_required(login_url='/accounts/login/')
def obtener_datos_correos(request, id):
    usuario = request.user
    grupo = Grupos.objects.filter(id=id).first()
    grupos = Grupos.objects.filter(propietario=usuario).exclude(id=id)
    nombre_grupos = [{'id': d.id, 'nombre': d.nombre} for d in grupos]
    plantillas = Plantillas.objects.filter(propietario=usuario)
    lista_plantillas = [{'id': d.id, 'nombre': d.nombre} for d in plantillas]
    correos = Correos.objects.filter(propietario=usuario, grupo__id=id)

    data_count = Data.objects.count()
    data_elements = Data.objects.values_list('id', 'fecha')

    # Convertir las fechas en formato de cadena
    data_elements = [(id, fecha.strftime('%Y-%m-%d')) for id, fecha in data_elements]

    datos = []
    for correo in correos:
        enviados = Enviados.objects.filter(propietario=usuario, correo=correo)

        correo_datos = {
            'correo': correo,
            'enviados': [],
            'grupos': nombre_grupos,
            'grupo': grupo.nombre,
            'grupo_id': grupo.id,
            'plantillas': lista_plantillas,
            'data_count': data_count,
            'data_elements': data_elements,
        }

        for enviado in enviados:
            estatus_web = Estatus_Web.objects.filter(enviado=enviado).first()
            estatus_mail = Estatus_Mail.objects.filter(enviado=enviado).first()
            estatus_pc = Estatus_PC.objects.filter(enviado=enviado).first()

            dato_enviado = {
                'enviado': enviado,
                'estatus_web': estatus_web,
                'estatus_mail': estatus_mail,
                'estatus_pc': estatus_pc,
            }

            correo_datos['enviados'].append(dato_enviado)

        datos.append(correo_datos)

    return datos








# Funciones post

@login_required(login_url='/accounts/login/')
def eliminar_correo(request):
    
    if request.POST['eliminar'] == 'eliminar':

        try:

            correo_obj = Correos.objects.filter(id=request.POST['id'])
            correo_obj.delete()
            messages.add_message(request, messages.SUCCESS, 'Correo eliminado correctamente')
        
        except:

            messages.add_message(request, messages.ERROR, 'No se ha encontrado el correo')
    
    else:

        messages.add_message(request, messages.ERROR, 'No se ha podido eliminar el correo')

    return 
    
@login_required(login_url='/accounts/login/')
def cambiar_correo_grupo(request):

    try:

        Correos.objects.filter(id=request.POST['id-correo']).update(grupo=request.POST['id-grupo'])

        messages.add_message(request, messages.SUCCESS, 'Correo movido correctamente')
    
    except:

        messages.add_message(request, messages.ERROR, 'No se ha encontrado el correo')
    

    return

@login_required(login_url='/accounts/login/')
def añadir_correo(request):
    usuario = request.user.username
    usuario = User.objects.get(username=usuario)
    comprabacion = Correos.objects.filter(correo=request.POST['correo'], propietario=usuario)
    if comprabacion: 
        messages.add_message(request, messages.ERROR, 'Error al añadir el correo o el correo ya existe')
    else:
        usuario = User.objects.get(username=usuario)
        grupo = Grupos.objects.get(id=request.POST['grupo'], propietario=usuario)
        Correos.objects.create(correo=request.POST['correo'], grupo=grupo, propietario=usuario)
        messages.add_message(request, messages.SUCCESS, 'Correo añadido correctamente')
    return 



@login_required(login_url='/accounts/login/')
def eliminar_registro(request):
    
    if request.POST['eliminar'] == 'eliminar':

        try:

            enviado = Enviados.objects.filter(id=request.POST['id'])
            enviado.delete()
            messages.add_message(request, messages.SUCCESS, 'Registro eliminado correctamente')
        
        except:

            messages.add_message(request, messages.ERROR, 'No se ha encontrado el registro')
    
    else:

        messages.add_message(request, messages.ERROR, 'No se ha podido eliminar el registro')

    return 