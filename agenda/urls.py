# agenda/urls.py

from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('', views.inicio, name='inicio_agenda'),
    path('agregar/', views.agregar_recordatorio, name='agregar_recordatorio'),
    path('listar/', views.listar_recordatorios, name='listar_recordatorios'),
    path('hoy/', views.recordatorios_hoy, name='recordatorios_hoy'),
    path('proximos/', views.recordatorios_proximos, name='recordatorios_proximos'),
    path('sin_realizar/', views.recordatorios_sin_realizar, name='recordatorios_sin_realizar'),
    path('vencidos/', views.recordatorios_vencidos, name='recordatorios_vencidos'),
    path('editar/<int:pk>/', views.editar_recordatorio, name='editar_recordatorio'),
    path('toggle_hecho/<int:pk>/', views.toggle_hecho, name='toggle_hecho'),
    path('recordar/', views.recordar_dia, name='recordar_dia'),
]
