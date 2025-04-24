# config/config/urls.py
from django.contrib import admin
from django.urls import path, include
from config import views as config_views  # Importamos la vista principal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', include('agenda.urls', namespace='agenda')),
    path('', config_views.index, name='home'),  # Ruta raíz que carga index.html
    path('gestion_usuarios/', include('gestion_usuarios.urls')),
    path('gestion_usu/', include('gestion_usuarios.urls', namespace='gestion_usuarios')),
    path('agenda/', include('agenda.urls')), 
    # Puedes agregar otras apps aquí si lo necesitas
]
