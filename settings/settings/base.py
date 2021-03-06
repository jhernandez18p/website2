import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('KEY')

if str(config('DEBUG')) == 'True':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ['*']

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'local_apps.dashboard',
    'local_apps.frontend',
    'local_apps.iurd',
    'local_apps.medias',
    'local_apps.news',
    'local_apps.profiles',
    'local_apps.testimonials',
    'local_apps.widgets',
]

THIRD_PARTY_APPS = [
    'ckeditor',
    'social_django',
    'rest_framework',
    'crispy_forms',
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir),'templates')),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'settings.settings.custom_context_processors.cookies',
                'settings.settings.custom_context_processors.menu',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

if DEBUG == True:
    WSGI_APPLICATION = 'settings.wsgi_local.application'
elif DEBUG == False:
    WSGI_APPLICATION = 'settings.wsgi_prod.application'

DATABASES = {
    'default': {
        'ENGINE': config('BASE_DB_ENGINE'),
        'NAME': config('BASE_DB_NAME'),
        'USER': config('BASE_DB_USER'),
        'PASSWORD': config('BASE_DB_PASSWORD'),
        'HOST': config('BASE_DB_HOST'),
        'PORT': '',
    }
}
       

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Panama'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir),'media'))

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir),'staticfiles')),
)

# STATIC_ROOT = os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir),'staticfiles'))

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
    'local_apps.profiles.EmailBackend.EmailBackend',
)

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = 'https://universal.org.pa'

LOGIN_URL = '/auth/entrar/'

SESSION_COOKIE_AGE = 43200

SESSION_COOKIE_NAME = 'iurd_session'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CUSTOM_TEMPLATES = (
    ('BASE','base/index.html'),
    ('ABOUT','base/about.html'),
    ('BLOG','base/blog.html'),
    ('CONTACT','base/contact.html'),
    ('PROJECTS','base/project.html'),
    ('REUNION','base/reunion.html'),
    ('TESTIMONIAL','base/testimonial.html'),
)
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# SOCIAL AUTH CONF
SOCIAL_AUTH_URL_NAMESPACE = 'social'
# GOOGLE BACKEND
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('GOOGLE_OAUTH2_SECRET')
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = []
# TWITTER BACKEND
SOCIAL_AUTH_TWITTER_KEY = config('TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET = config('TWITTER_SECRET')
# FACEBOOK BACKEND
SOCIAL_AUTH_FACEBOOK_KEY = config('FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = config('FACEBOOK_SECRET')
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'locale': 'es',
    'fields': 'id, name, email, age_range'
}


""" Email Conf.             """
EMAIL_HOST = config("EMAIL_HOST",)
EMAIL_PORT = config("EMAIL_PORT", cast=int)
EMAIL_HOST_USER = config("EMAIL_HOST_USER",)
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD",)
EMAIL_USE_SSL = True


"""
    Rest API
"""
REST_FRAMEWORK = {
    #'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser','rest_framework.permissions.IsAuthenticated','rest_framework.permissions.AllowAny',),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
    'PAGE_SIZE': 10
}
