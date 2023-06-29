from django.db import models
from django.contrib.auth.models import User
from backend.opciones.models import Emisores

# Create your models here.
 

class Plantillas(models.Model):


    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField()
    imagen = models.ImageField(upload_to='imagenes')
    plantilla = models.TextField()
    script = models.TextField()
    icono = models.ImageField(upload_to='imagenes')
    pdf = models.FileField(upload_to='imagenes')
    emisor = models.ForeignKey(Emisores, on_delete=models.CASCADE)
    propietario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)  

    def __str__(self):
        return self.nombre
    
