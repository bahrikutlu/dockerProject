import os
import environ
from .database import DATABASES, BASE_DIR
from .admins_list import ADMINS_LIST
import warnings
import re


env = environ.Env()
with warnings.catch_warnings(record=True) as w:
    environ.Env.read_env()

env_file_is_missing = True if len(w) == 1 else False

print(f"Development environment, getting the variable from servers environment variables") if env_file_is_missing else None

DEBUG = os.environ.get('DEBUG', False) if env_file_is_missing else env.bool('DEBUG')

SECRET_KEY = os.environ.get('SECRET_KEY', '1234') if env_file_is_missing else env('SECRET_KEY')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', ['127.0.0.1']) if env_file_is_missing else env('ALLOWED_HOSTS').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS += [
    'core',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "build")],
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

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = DATABASES

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', }, ]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEBUG = os.environ.get('DEBUG', False) if env_file_is_missing else env.bool('DEBUG')

# EMAIL SETTINGS
EMAIL_HOST = os.environ.get('EMAIL_HOST', False) if env_file_is_missing else env('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT', False) if env_file_is_missing else env('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', False) if env_file_is_missing else env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', False) if env_file_is_missing else env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', False) if env_file_is_missing else env('DEFAULT_FROM_EMAIL')

# Email Configuration
ADMINS = ADMINS_LIST
MANAGERS = ADMINS

IGNORABLE_404_URLS = [
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
]

