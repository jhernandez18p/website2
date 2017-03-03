from settings.settings.base import *
from decouple import config

WSGI_APPLICATION = 'settings.wsgi_production.application'

ALLOWED_HOSTS = ['universal.org.pa','www.universal.org.pa','universalpanama.com','www.universalpanama.com']

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': '',
    }
}