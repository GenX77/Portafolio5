# config/urls.py

from django.contrib import admin
from django.urls import path, include
from config import views as config_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', config_views.index, name='home'),  # Vista principal corregida

]
