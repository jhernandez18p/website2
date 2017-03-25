from settings.settings.base import *
from decouple import config


ALLOWED_HOSTS = ['universal.org.pa','www.universal.org.pa','universalpanama.com','www.universalpanama.com']

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

""" Email Conf.             """

EMAIL_HOST = config("EMAIL_HOST",)
EMAIL_PORT = config("EMAIL_PORT", cast=int)
EMAIL_HOST_USER = config("EMAIL_HOST_USER",)
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD",)
EMAIL_USE_SSL = config("EMAIL_USE_SSL", cast=bool)

""" SSL Conf. """
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
