from django.contrib.auth.models import User, Group
from django.shortcuts import render
from settings.settings.serializers import UserSerializer, GroupSerializer

from rest_framework import viewsets
from local_apps.iurd.models import *
from local_apps.medias.models import *
from local_apps.news.models import *
from local_apps.testimonials.models import *
# Create your views here.

def home(request):

	template = 'base/index.html'
	context = {
		'pg_title':'Inicio',
	}

	try:
		news = Post.objects.all()
		last_new = {}
		last_new['title'] = news.last()
		last_new['image'] = news.last().image
		last_new['slug'] = news.last().slug
		if len(news)>6:
			news = news[-1]
		context['last_news'] = last_new
		context['news'] = news
	except Exception as e:
		print('No hay noticias aún')

	try:
		feeds = Feed.objects.all()
		context['feeds'] = feeds[:6]
	except Exception as e:
		print('No hay blogs amigos aún')

	try:
		video = Video.objects.all().filter(active=True)
		context['videos'] = video
	except Exception as e:
		print('No hay videos aún')

	try:
		audio = Audio.objects.all().filter(active=True)
		context['audios'] = audio
	except Exception as e:
		print('No hay audios aún')

	try:
		imagen = Image.objects.all().filter(active=True)
		context['imagen'] = imagen
	except Exception as e:
		print('No hay imgen aún')

	try:
		testimonials = Testimonial.objects.all()
		context['testimonials'] = testimonials
	except Exception as e:
		print('No hay Testimonios aún')


	return render(request, template, context)


def about(request):
	template = 'base/about.html'
	context = {
		'pg_title':'',
	}
	return render(request, template, context)


def projects(request):
	template = 'base/project.html'
	context = {
		'pg_title':'',
	}
	return render(request, template, context)


def reunions(request):
	template = 'base/reunion.html'
	context = {
		'pg_title':'',
	}
	return render(request, template, context)


def testimonials(request):
	template = 'base/testimonial.html'
	context = {
		'pg_title':'',
	}
	return render(request, template, context)


def media(request):
	template = 'base/media.html'
	context = {
		'pg_title':'',
	}
	return render(request, template, context)


def blog(request):
	template = 'base/media.html'
	context = {
		'pg_title':'',
	}
	return render(request, template, context)


def contact(request):
	template = 'base/contact.html'
	context = {
		'pg_title':'',
	}
	return render(request, template, context)


"""
	Rest API
"""

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer