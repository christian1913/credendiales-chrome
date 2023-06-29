from django.contrib import admin
from backend.registradores.models import Estatus_Mail, Estatus_PC, Estatus_Web, ZipFile

# Register your models here.

admin.site.register(Estatus_Mail)
admin.site.register(Estatus_Web)
admin.site.register(Estatus_PC)
admin.site.register(ZipFile)