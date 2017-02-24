from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from local_apps.dashboard import views as dashboard_views

urlpatterns = [
	url(r'^$', dashboard_views.home, name='Home'),
	url(r'^quienes-somos/', dashboard_views.post_church, name='About'),
	url(r'^proyectos/', dashboard_views.projects, name='Projects'),
	url(r'^reuniones/', dashboard_views.reunions, name='Reunions'),
	url(r'^testimonios/', dashboard_views.testimonials, name='Testimonials'),
	url(r'^multimedia/', dashboard_views.media, name='Media'),
	url(r'^noticias/', dashboard_views.blog, name='Blog'),
	url(r'^contacto/', dashboard_views.contact, name='Contact'),
]