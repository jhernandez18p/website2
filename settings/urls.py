from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers

from local_apps.profiles.auth import (login,register,logout)
from local_apps.frontend import views as base_views

router = routers.DefaultRouter()
router.register(r'api/users', base_views.UserViewSet)
router.register(r'api/groups', base_views.GroupViewSet)

urlpatterns = [
	url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^',include('local_apps.frontend.urls' ,namespace='frontend')),
	url(r'^dashboard/',include('local_apps.dashboard.urls' ,namespace='dashboard')),
    url(r'^-admin/', admin.site.urls),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)