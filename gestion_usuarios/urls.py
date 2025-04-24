# gestion_usuarios/urls.py

from django.urls import path
from . import views

app_name = 'gestion_usuarios'  # <-- ¡ESTA LÍNEA ES CRUCIAL!

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.agregar_contacto, name='agregar_contacto'),
    path('listar/', views.listar_contactos, name='listar_contactos'),
    path('modificar/<int:contacto_id>/', views.modificar_contacto, name='modificar_contacto'),
    path('buscar/', views.buscar_contactos, name='buscar_contactos'),
    path('eliminar/<int:contacto_id>/', views.eliminar_contacto, name='eliminar_contacto'),
]
