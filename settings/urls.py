from django.conf import settings
from django.conf.urls import (include, url, handler400, handler403, handler404, handler500)
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers

from local_apps.profiles.auth import (login,register,logout,activate)
from local_apps.frontend import views as base_views

router = routers.DefaultRouter()
router.register(r'api/users', base_views.UserViewSet)
router.register(r'api/groups', base_views.GroupViewSet)
router.register(r'api/church', base_views.ChurchViewSet)

handler400 = 'local_apps.frontend.views.my_custom_bad_request_view'
handler403 = 'local_apps.frontend.views.my_custom_permission_denied_view'
handler404 = 'local_apps.frontend.views.my_custom_page_not_found_view'
handler500 = 'local_apps.frontend.views.my_custom_error_view'

urlpatterns = [

	url(r'^',include('local_apps.frontend.urls' ,namespace='frontend')),
	url(r'^auth/',include('local_apps.profiles.urls' ,namespace='auth')),
    url(r'^dashboard/',include('local_apps.dashboard.urls' ,namespace='dashboard')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),

    url(r'^', include(router.urls)),
    url(r'^iurd/admin/', admin.site.urls),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)