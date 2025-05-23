# config/config/settings.py — configuración adaptativa para entorno local y producción (Render)

from pathlib import Path
from decouple import config
import dj_database_url
import os
import socket

# Establecemos la base del directorio
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Cargamos la clave secreta y la configuración del entorno
SECRET_KEY = config('SECRET_KEY', default='unsafe-default-key')
DEBUG = config('DEBUG', default=False, cast=bool)

# Permitimos los hosts que puedan acceder al proyecto
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')], default='127.0.0.1,localhost')

# Apps instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
]

# Middleware configurado para el proyecto
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL principal de configuración
ROOT_URLCONF = 'config.urls'

# Configuración de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Asegúrate de que la carpeta 'templates' exista
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI configuration
WSGI_APPLICATION = 'config.wsgi.application'

# Detectar si estamos en Render por nombre de host
IS_RENDER = socket.gethostname().startswith('render')

# Configuración de la base de datos según el entorno
if IS_RENDER:
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Validadores de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Configuración de lenguaje y zona horaria
LANGUAGE_CODE = 'es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configuración de archivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configuración de campo automático por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
