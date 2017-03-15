from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from settings.settings.serializers import UserSerializer, GroupSerializer
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
		'pg_title':'home',
		'title':'Inicio',
	}

	try:
		news = Post.objects.active()[:10]
		if len(news)>=1:
			last_new = news.first()
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
		video = Video.objects.all().filter(active=True)[:1]
		context['videos'] = video
	except Exception as e:
		print('No hay videos aún' + e)

	try:
		audio = Audio.objects.all().filter(active=True)
		context['audios'] = audio
	except Exception as e:
		print('No hay audios aún' + e)

	try:
		imagen = Image.objects.all().filter(active=True)[:1] 
		context['imagen'] = imagen
	except Exception as e:
		print('No hay imgen aún' + e)

	try:
		testimonials = Testimonial.objects.all()
		context['testimonials'] = testimonials
	except Exception as e:
		print('No hay Testimonios aún' + e)

	try:
		projects = Project.objects.all().filter(project_type='Projecs')
		# if len(projects)>0:
		# 	print(projects[0].category)
		context['projects'] = projects
	except Exception as e:
		print('No hay proyectos aún' + e)

	try:
		groups = Project.objects.all().filter(project_type='Groups')
		# if len(groups)>0:
		# 	print(groups[0].category)
		context['groups'] = groups
	except Exception as e:
		print('No hay grupos aún' + e)

	return render(request, template, context)


def about(request):
	template = 'base/about.html'
	context = {
		'pg_title':'about',
		'title':'¿Quienes somos?',
	}
	return render(request, template, context)


def projects(request):
	template = 'base/project.html'
	context = {
		'pg_title':'project',
		'title':'Proyectos universal',
	}
	try:
		projects = Project.objects.all().filter(project_type='Projecs')
		# if len(projects)>0:
		# 	print(projects[0].category)
		context['projects'] = projects
	except Exception as e:
		print('No hay proyectos aún' + e)

	try:
		groups = Project.objects.all().filter(project_type='Groups')
		# if len(groups)>0:
		# 	print(groups[0].category)
		context['groups'] = groups
	except Exception as e:
		print('No hay grupos aún' + e)

	return render(request, template, context)


def reunions(request):
	template = 'base/reunion.html'
	reunions = Reunion.objects.all()
	context = {
		'pg_title':'reunion',
		'title':'Reuniones',
		'objects':reunions,
	}
	return render(request, template, context)


def testimonials(request):
	template = 'base/testimonial.html'
	context = {
		'pg_title':'testimonial',
		'title':'Testimonios',
	}

	try:
		testimonials = Testimonial.objects.all()
		testimonial_list = testimonials
		testimonials = testimonials[:5]
		context['testimonials'] = testimonials
	except Exception as e:
		print('No hay Testimonios aún' + e)
	
	page = request.GET.get('page', 1)
	paginator = Paginator(testimonial_list, 12)
	try:
		testimonial_list = paginator.page(page)
	except PageNotAnInteger:
		testimonial_list = paginator.page(1)
	except EmptyPage:
		testimonial_list = paginator.page(paginator.num_pages)

	context['testimonial_list'] = testimonial_list

	return render(request, template, context)


def media(request):
	template = 'base/media.html'
	context = {
		'pg_title':'media',
		'title':'Multimedia',
	}

	try:
		videos = Video.objects.all()
		video_list = videos
		context['videos'] = videos
	except Exception as e:
		print('No hay videos aún' + e)
	
	page = request.GET.get('page', 1)
	paginator = Paginator(video_list, 12)
	try:
		video_list = paginator.page(page)
	except PageNotAnInteger:
		video_list = paginator.page(1)
	except EmptyPage:
		video_list = paginator.page(paginator.num_pages)

	context['video_list'] = video_list

	try:
		audios = Audio.objects.all()
		context['audios'] = audios
	except Exception as e:
		print(e)
		print('Aún no hay audios')
	
	try:
		newspapers = Newspaper.objects.all()
		newspaper_list = newspapers
		context['newspapers'] = newspapers
	except Exception as e:
		print('No hay newspapers aún' + e)
	
	page = request.GET.get('page', 1)
	paginator = Paginator(newspaper_list, 5)
	try:
		newspaper_list = paginator.page(page)
	except PageNotAnInteger:
		newspaper_list = paginator.page(1)
	except EmptyPage:
		newspaper_list = paginator.page(paginator.num_pages)

	context['newspaper_list'] = newspaper_list

	try:
		events = Event.objects.all()
		context['events'] = events
	except Exception as e:
		print(e)
		print('Aún no hay eventos')

	return render(request, template, context)


def blog(request):
	template = 'base/blog.html'
	context = {
		'pg_title':'blog',
		'title':'Noticias',
	}

	try:
		categories = Category.objects.all()
		context['categories'] = categories
	except Exception as e:
		print('No hay categorias aún' + e)

	try:
		news = Post.objects.all()
		news_list = news
		context['news'] = news
	except Exception as e:
		print('No hay noticias aún' + e)
	
	page = request.GET.get('page', 1)
	paginator = Paginator(news_list, 10)
	try:
		news_list = paginator.page(page)
	except PageNotAnInteger:
		news_list = paginator.page(1)
	except EmptyPage:
		news_list = paginator.page(paginator.num_pages)

	context['news_list'] = news_list

	return render(request, template, context)


def events(request):
	template = 'base/events.html'
	context = {
		'pg_title':'events',
		'title':'Eventos',
	}

	try:
		events = Event.objects.all()
		context['events'] = events
	except Exception as e:
		raise e

	return render(request, template, context)


def contact(request):
	template = 'base/contact.html'
	context = {
		'pg_title':'contact',
		'title':'Contato',
	}

	if request.method == 'GET':

		return render(request, template, context)

	elif request.method == 'POST':
		
		name = request.POST['name']
		email = 'desconocido'
		email = request.POST['email']
		phone = 'desconocido'
		phone = request.POST['phone']
		description = request.POST['description']
		submit = request.POST['submit']
		url = request.POST['url']

		if submit == 'True':
			if name == '' or description == '':
				return HttpResponseRedirect(url)
			# print(' %s\n %s\n %s\n' %(name,email,description))
			new = Subscriber.objects.create(name=name,email=email,phone=phone,description=description)
			new.save()
			if email != 'desconocido':
				print('enviar correo a {}'.format(email))
			else:
				print('No enviar correo')
			context['messages'] = True
			send_mail(
		            'Mensaje contacto Pagina web \"Iglesia Universal del Reino de Dios\"',
		            '%s, %s, %s, %s' % (str(name),str(email),str(phone),str(description)) ,
		            config("EMAIL_HOST_USER",),
		            [config("EMAIL_HOST_USER",)],
		            fail_silently=False,
		        )
			return render(request, template, context)

		else:
			request.session['user_rouge_for_pray'] = False
			return HttpResponseRedirect(url)


"""
	Rouge for pray
"""
def susbcribe(request):
	if request.method == 'GET':

		return HttpResponseRedirect(request.get_full_path)

	elif request.method == 'POST':
		
		name = request.POST['name']
		email = request.POST['email']
		description = request.POST['description']
		submit = request.POST['submit']
		url = request.POST['url']

		if submit == 'True':
			if name == '' or email == '' or description == '':
				return HttpResponseRedirect(url)
			print(' %s\n %s\n %s\n' %(name,email,description))
			new = Subscriber.objects.create(name=name,email=email,description=description)
			new.save()
			return HttpResponseRedirect(url)

		else:

			request.session['user_rouge_for_pray'] = False
			return HttpResponseRedirect(url)


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


"""
	custom errors
"""
def my_custom_bad_request_view(request):
	template = 'url_error/frontend/400.html'
	context = {
		'pg_title':'Error 400',
		'title':'Error 400',
	}
	return render(request, template, context)


def my_custom_permission_denied_view(request):
	template = 'url_error/frontend/403.html'
	context = {
		'pg_title':'Error 403',
		'title':'Error 403',
	}
	return render(request, template, context)


def my_custom_page_not_found_view(request):
	template = 'url_error/frontend/404.html'
	context = {
		'pg_title':'Error 404',
		'title':'Error 404',
	}
	return render(request, template, context)


def my_custom_error_view(request):
	template = 'url_error/frontend/500.html'
	context = {
		'pg_title':'Error 500',
		'title':'Error 500',
	}
	return render(request, template, context)


"""
	Details
"""
def blog_detail(request, slug):
	template = 'detail/blogs.html'
	new = get_object_or_404(Post, slug=slug)
	title = (new.title)
	try:
		comments = Comment.objects.all().filter(content_type=new.get_content_type, object_id=new.id)
		print(comments)
	except Exception as e:
		print(e)

	
	context = {
		'pg_title':'blog',
		'title':'Detalles {}'.format(str(title)),
		'post':new,
		'comments':comments,
	}

	return render(request, template, context)


def blog_filter(request, category):
	template = 'base/blog.html'
	title = 'Filtro de categorias'
	context = {
		'pg_title':'blog',
		'title':'Detalles {}'.format(str(title)),
	}
	try:
		news = Post.objects.all().filter(category=category)
		news_list = news
		context['news'] = news
	except Exception as e:
		print('No hay noticias aún' + e)
	
	page = request.GET.get('page', 1)
	paginator = Paginator(news_list, 10)
	try:
		news_list = paginator.page(page)
	except PageNotAnInteger:
		news_list = paginator.page(1)
	except EmptyPage:
		news_list = paginator.page(paginator.num_pages)

	context['news_list'] = news_list
	

	return render(request, template, context)


def projects_detail(request, pk):
	template = 'detail/projects.html'
	project = get_object_or_404(Project, id=pk)
	print(project)
	title = project.title
	
	context = {
		'pg_title':'project',
		'title':'Detalles {}'.format(str(title)),
		'project':project,
	}

	return render(request, template, context)


def reunions_detail(request, pk):
	template = 'detail/reunions.html'
	reunions = get_object_or_404(Reunion,id=pk)
	title = ''
	
	context = {
		'pg_title':'reunion',
		'title':'Detalles {}'.format(str(title)),
		'object':reunions,
	}

	return render(request, template, context)


def testimonials_detail(request, pk):
	template = 'detail/testimonials.html'
	testimonial = get_object_or_404(Testimonial,id=pk)
	title = testimonial.title
	
	context = {
		'pg_title':'testimonial',
		'title':'Detalles {}'.format(str(title)),
		'object':testimonial
	}

	return render(request, template, context)


def events_detail(request, pk):
	template = 'detail/events.html'
	event = get_object_or_404(Event, id=pk)
	title = event.title
	
	context = {
		'pg_title':'events',
		'title':'Detalles {}'.format(str(title)),
		'object':event,
	}

	return render(request, template, context)

