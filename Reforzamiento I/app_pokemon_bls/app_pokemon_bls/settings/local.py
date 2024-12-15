from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nxmmc4=toswbnlbekt*ae0)m&2(t_6y9&ghmf-bitmjvey*tw='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_pokemon_app_bls',
        'USER': 'postgres',
        'PASSWORD': '2#DCXSJZ-zjlET7uQU/8',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
