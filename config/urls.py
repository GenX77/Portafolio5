# config/urls.py

from django.contrib import admin
from django.urls import path, include
from config import views as config_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', include('agenda.urls', namespace='agenda')),
    path('', config_views.index, name='home'),
    path('gestion_usuarios/', include('gestion_usuarios.urls')),
    path('gestion_usu/', include('gestion_usu.urls')),
]
