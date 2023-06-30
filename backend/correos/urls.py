from django.urls import path
from . import views

urlpatterns = [

    # Paginas

    path('grupos/<str:id>', views.index, name='correos'),
    path('enviar-archivo/<str:id>', views.enviar_archivo, name='enviar_archivo'),

    
]
