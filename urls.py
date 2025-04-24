# config/urls.py — rutas principales del proyecto

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hola_mundo, name='index'),

    path('usuarios/', include('gestion_usuarios.urls', namespace='gestion_usuarios')),
    path('usu/', include('gestion_usu.urls', namespace='gestion_usu')),
    path('contactos/', include('gestion_contactos.urls', namespace='gestion_contactos')),
]
