from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from local_apps.frontend import views as base_views

urlpatterns = [

	url(r'^$', base_views.home, name='Home'),
	url(r'^contacto/', base_views.contact, name='Contact'),
	url(r'^suscribirse/', base_views.susbcribe, name='Pray'),
	url(r'^quienes-somos/', base_views.about, name='About'),

	url(r'^multimedia/periodico/(?P<pk>[\w-]+)/', base_views.newspaper, name='Newspaper'),
	url(r'^multimedia/', base_views.media, name='Media'),

	url(r'^eventos/(?P<pk>[\w-]+)', base_views.events_detail, name='Event_detail'),
	url(r'^eventos/', base_views.events, name='Events'),

	url(r'^noticias/categoria/(?P<category>[\w-]+)/', base_views.blog_filter, name='Blog_category'),
	url(r'^noticias/(?P<slug>[\w-]+)/', base_views.blog_detail, name='Blog_details'),
	url(r'^noticias/', base_views.blog, name='Blog'),
	
	url(r'^proyectos/(?P<name>[\w-]+)/', base_views.projects_detail, name='Project_detail'),
	url(r'^proyectos/', base_views.projects, name='Projects'),

	url(r'^reuniones/(?P<pk>[\w-]+)/', base_views.reunions_detail, name='Reunions_detail'),
	url(r'^reuniones/', base_views.reunions, name='Reunions'),

	url(r'^testimonios/(?P<pk>[\w-]+)/', base_views.testimonials_detail, name='Testimonial_detail'),
	url(r'^testimonios/', base_views.testimonials, name='Testimonials'),
]