from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from settings.settings.serializers import UserSerializer, GroupSerializer
import random

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
		news = Post.objects.active()[:10]
		if len(news)>=1:
			last_new = {}
			last_new['title'] = news.first()
			last_new['image'] = news.first().image
			last_new['slug'] = news.first().slug
		context['last_news'] = last_new
		context['news'] = news
	except Exception as e:
		print(e)
		print('No hay noticias aún' + e)

	try:
		feeds = Feed.objects.all()
		context['feeds'] = feeds[:6]
	except Exception as e:
		print('No hay blogs amigos aún' + e)

	try:
		video = Video.objects.all().filter(active=True)
		context['videos'] = video
	except Exception as e:
		print('No hay videos aún' + e)

	try:
		audio = Audio.objects.all().filter(active=True)
		context['audios'] = audio
	except Exception as e:
		print('No hay audios aún' + e)

	try:
		imagen = Image.objects.all().filter(active=True)
		context['imagen'] = imagen
	except Exception as e:
		print('No hay imgen aún' + e)

	try:
		testimonials = Testimonial.objects.all()
		context['testimonials'] = testimonials
	except Exception as e:
		print('No hay Testimonios aún' + e)

	try:
		projects = Project.objects.all().filter(category='Projecs')
		if len(projects)>0:
			print(projects[0].category)
		context['projects'] = projects
	except Exception as e:
		print('No hay proyectos aún' + e)

	try:
		groups = Project.objects.all().filter(category='Groups')
		if len(groups)>0:
			print(groups[0].category)
		context['groups'] = groups
	except Exception as e:
		print('No hay grupos aún' + e)

	return render(request, template, context)


def about(request):
	template = 'base/about.html'
	context = {
		'pg_title':'¿Quienes somos?',
	}
	return render(request, template, context)


def projects(request):
	template = 'base/project.html'
	context = {
		'pg_title':'Proyectos universal',
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
	template = 'base/blog.html'
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