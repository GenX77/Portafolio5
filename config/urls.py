# config/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Incluye la app gestion_usuarios
    path('usuarios/', include('gestion_usuarios.urls', namespace='gestion_usuarios')),

    # Incluye la app gestion_usu
    path('usu/', include('gestion_usu.urls', namespace='gestion_usu')),

    # Incluye la app gestion_contactos
    path('contactos/', include('gestion_contactos.urls', namespace='gestion_contactos')),
]
