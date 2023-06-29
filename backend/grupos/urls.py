from django.urls import path
from . import views

urlpatterns = [

    # Paginas

    path('', views.index, name='grupos'),

    
]