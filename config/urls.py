# config/urls.py

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hola_mundo, name='index'),

    # Incluye la app gestion_usuarios
    path('usuarios/', include('gestion_usuarios.urls', namespace='gestion_usuarios')),

    # Incluye la app gestion_usu
    path('usu/', include('gestion_usu.urls', namespace='gestion_usu')),
]
