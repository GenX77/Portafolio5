# config/urls.py — rutas principales del proyecto

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hola_mundo, name='index'),

    
