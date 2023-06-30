from django.db import models
from django.contrib.auth.models import User
from backend.smtp.models import Enviados


# Create your models here.



class Estatus_Mail(models.Model):
    ip = models.GenericIPAddressField(blank=True, null=True)
    agente = models.TextField(blank=True, null=True)
    pais = models.CharField(max_length=100,blank=True, null=True)
    metodo = models.CharField(max_length=10,blank=True, null=True)
    parametros = models.TextField(blank=True, null=True)
    sistema_operativo = models.CharField(max_length=100,blank=True, null=True)
    dispositivo = models.CharField(max_length=100,blank=True, null=True)
    idioma = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    enviado = models.ForeignKey(Enviados, on_delete=models.CASCADE)


    def __str__(self):
        return f'LogEntry #{self.id}'

class Estatus_Web(models.Model):
    ip = models.GenericIPAddressField(blank=True, null=True)
    agente = models.TextField(blank=True, null=True)
    pais = models.CharField(max_length=100,blank=True, null=True)
    metodo = models.CharField(max_length=10,blank=True, null=True)
    parametros = models.TextField(blank=True, null=True)
    sistema_operativo = models.CharField(max_length=100,blank=True, null=True)
    dispositivo = models.CharField(max_length=100,blank=True, null=True)
    idioma = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    enviado = models.ForeignKey(Enviados, on_delete=models.CASCADE)


    def __str__(self):
        return f'LogEntry #{self.id}'
    
class Estatus_PC(models.Model):
    ip = models.GenericIPAddressField(blank=True, null=True)
    agente = models.TextField(blank=True, null=True)
    pais = models.CharField(max_length=100,blank=True, null=True)
    metodo = models.CharField(max_length=10,blank=True, null=True)
    parametros = models.TextField(blank=True, null=True)
    sistema_operativo = models.CharField(max_length=100,blank=True, null=True)
    dispositivo = models.CharField(max_length=100,blank=True, null=True)
    idioma = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    enviado = models.ForeignKey(Enviados, on_delete=models.CASCADE)


    def __str__(self):
        return f'LogEntry #{self.id}'
    


class ZipFile(models.Model):
    name = models.CharField(max_length=255)
    enviado = models.ForeignKey(Enviados, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Data(models.Model):
    data = models.TextField()
    fecha = models.DateField(auto_now=True)
