from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers

from local_apps.profiles.auth import (login,register,logout,activate)
from local_apps.frontend import views as base_views

router = routers.DefaultRouter()
router.register(r'api/users', base_views.UserViewSet)
router.register(r'api/groups', base_views.GroupViewSet)

urlpatterns = [
	url(r'^',include('local_apps.frontend.urls' ,namespace='frontend')),
	url(r'^dashboard/',include('local_apps.dashboard.urls' ,namespace='dashboard')),
    url(r'^iurd/admin/', admin.site.urls),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^entrar/', login , name='Login'),
    url(r'^registro/', register , name='Register'),
    url(r'^salir/', logout , name='Logout'),
	url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)