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
	news = Post.objects.all()
	latest_news = news.last()
	template = 'base/index.html'
	context = {
		'pg_title':'',
		'last_news':latest_news,
	}
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