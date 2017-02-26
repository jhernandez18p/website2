from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from local_apps.frontend import views as base_views

urlpatterns = [
	url(r'^$', base_views.home, name='Home'),
	url(r'^quienes-somos/', base_views.about, name='About'),
	url(r'^proyectos/', base_views.projects, name='Projects'),
	url(r'^reuniones/', base_views.reunions, name='Reunions'),
	url(r'^testimonios/', base_views.testimonials, name='Testimonials'),
	url(r'^multimedia/', base_views.media, name='Media'),
	url(r'^multimedia/eventos/(?P<slug>[\w-]+)/', base_views.events, name='Events'),
	url(r'^noticias/', base_views.blog, name='Blog'),
	url(r'^noticias/(?P<slug>[\w-]+)/', base_views.blog_detail, name='Blog_detalle'),
	url(r'^contacto/', base_views.contact, name='Contact'),
	url(r'^suscribirse/', base_views.susbcribe, name='Pray'),
]