from django.shortcuts import render

from local_apps.iurd.forms import (ChurchForm,EventForm,FeedForm,ProjectForm,ScheduleForm,ReunionForm)

# Create your views here.
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
