# gestion_usu/urls.py

from django.urls import path
from . import views

app_name = 'gestion_usu'

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.agregar_usuario, name='agregar_usuario'),
    path('buscar/', views.buscar_usuarios, name='buscar_usuarios'),
    path('editar/<int:indice>/', views.editar_usuario, name='editar_usuario'),
    path('borrar/<int:indice>/', views.borrar_usuario, name='borrar_usuario'),
]
