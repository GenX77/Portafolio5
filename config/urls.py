# config/urls.py

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta principal que carga la vista index
    path('admin/', admin.site.urls),
    path('usuarios/', include(('gestion_usuarios.urls', 'gestion_usuarios'), namespace='gestion_usuarios')),
    path('usu/', include(('gestion_usu.urls', 'gestion_usu'), namespace='gestion_usu')),
]
