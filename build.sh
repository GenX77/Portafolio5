#!/usr/bin/env bash
set -o errexit  # Detiene el script si ocurre un error

# Instalar dependencias del proyecto
pip install -r requirements.txt

# Recolectar archivos estáticos (CSS, JS, imágenes, etc.)
python manage.py collectstatic --no-input

# Aplicar migraciones de base de datos
python manage.py migrate

# Crear superusuario automáticamente (si se define la variable de entorno CREATE_SUPERUSER)
# Para habilitar esto, descomenta las líneas siguientes y define las variables necesarias en Render:
# DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD

# if [[ $CREATE_SUPERUSER ]]; then
#     python manage.py createsuperuser --no-input
# fi
