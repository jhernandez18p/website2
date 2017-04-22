from settings.settings.base import *
from decouple import config


ALLOWED_HOSTS = ['universal.org.pa','www.universal.org.pa']

DATABASES = {
    'default': {
        'ENGINE': config('PROD_DB_ENGINE'),
        'NAME': config('PROD_DB_NAME'),
        'USER': config('PROD_DB_USER'),
        'PASSWORD': config('PROD_DB_PASSWORD'),
        'HOST': config('PROD_DB_HOST'),
        'PORT': '',
    }
}

