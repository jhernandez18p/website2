from django.conf.urls import url
from django.contrib import admin

from local_apps.profiles.auth import (login, logout, register, activate)

urlpatterns = [
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate, name='Activate'),
    url(r'^entrar/', login , name='Login'),
    url(r'^registro/', register , name='Register'),
    url(r'^salir/', logout , name='Logout'),
]
