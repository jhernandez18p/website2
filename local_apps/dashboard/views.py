from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from settings.settings.serializers import UserSerializer, GroupSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random

from rest_framework import viewsets
from local_apps.iurd.models import *
from local_apps.medias.models import *
from local_apps.news.models import *
from local_apps.testimonials.models import *
from local_apps.iurd.forms import (ChurchForm,EventForm,FeedForm,ProjectForm,ScheduleForm,ReunionForm)




# Create your views here.
@login_required
def home(request):
	template = 'dashboard/index.html'
	context = {
		'pg_title':'',
	}
	return render(request,template,context)

def post_church(request):
	template = 'dashboard/form.html'
	ChurchForm = ChurchForm(request.POST or None, request.FILES or None)

	context = {
		'pg_title':'',
		'form':ChurchForm,
	}
	return render(request,template,context)

def projects(request):
	template = 'dashboard/index.html'
	context = {
		'pg_title':'',
	}
	return render(request,template,context)

def reunions(request):
	template = 'dashboard/index.html'
	context = {
		'pg_title':'',
	}
	return render(request,template,context)

def testimonials(request):
	template = 'dashboard/index.html'
	context = {
		'pg_title':'',
	}
	return render(request,template,context)

def blog(request):
	template = 'dashboard/index.html'
	context = {
		'pg_title':'',
	}
	return render(request,template,context)

def media(request):
	template = 'dashboard/index.html'
	context = {
		'pg_title':'',
	}
	return render(request,template,context)

def contact(request):
	template = 'dashboard/index.html'
	context = {
		'pg_title':'',
	}
	return render(request,template,context)
