from settings.settings.base import LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL
from django.shortcuts import render, redirect
from django.contrib import auth
from django.core.mail import send_mail
from decouple import config
from django.contrib.auth.decorators import user_passes_test

def login(request):
	if request.method == 'GET':
		return render(request, 'auth/login.html',{'title':'Iniciar Sesión'})
	elif request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate( username = username, password = password)
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				next = ''
				if 'next' in request.GET:
					next = request.GET['next']
				if next == None or next == '':
					next = LOGIN_REDIRECT_URL
				return redirect(next)
			else:
				return render(request, 'auth/login.html', {
						'warning': 'Su cuenta ha caducado.',
						'title':'Iniciar Sesión',
					})
		else:
			return render(request, 'auth/login.html',{
							'warning': 'Usuario o contraseña erronea',
							'title':'Iniciar Sesión',
							})

def register(request):
	""" #Funcion que permite registrar usuarios al sitio web """
	error_template = 'auth/register.html'
	if request.method == 'POST' :
		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if username == '':
			context = {
				'title':'Error de Registro',
				'error':{
					'title':'Nombre de usuario requerido!',
					'error':'show',
					'email':'El campo de correo no puede estar vacio, recuerde que debe terminar en "@universal.org.pa"',
					'contacto':'Por favor contactar al administrador de sistemas, info@universal.org.pa'
				}
			}
			return render(request,error_template,context)

		if email == '':
			context = {
				'title':'Error de Registro',
				'error':{
					'title':'Email requerido!',
					'error':'show',
					'email':'El campo de correo no puede estar vacio, recuerde que debe terminar en "@universal.org.pa"',
					'contacto':'Por favor contactar al administrador de sistemas, info@universal.org.pa'
				}
			}
			return render(request,error_template,context)

		if password1 != password2:
			context = {
				'title':'Error de Registro',
				'error':{
					'title':'Contraseña inconsistente',
					'error':'show',
					'email':'Error "%s" no es igual a "%s"' % (password1,password2),
					'contacto':'Por favor contactar al administrador de sistemas, info@universal.org.pa',
					'input':'has-error',
				}
			}
			return render(request,error_template,context)

		# LLamamos al formulario de usuario desde el ORM.
		auth.models.User.objects.create_user(username,email,password2).save()
		user = auth.authenticate(username = username, password = password2)
		auth.login(request, user)
		send_mail(
		            'Registro de usuario',
		            '%s, %s' % (username,email) ,
		            config("DEV2TECH_EMAIL_HOST_USER",),
		            [config("DEV2TECH_EMAIL_HOST_USER",)],
		            fail_silently=False,
		        )
		context = {'title':'registro completo'}
		return render(request,LOGIN_REDIRECT_URL,context)

	elif request.method == 'GET':

		template = 'auth/register.html'
		context ={
			'title':'Registro',
			'error':{
				'error':'hide',
			}
		}
		return render(request, template, context)


def logout(request):

	auth.logout(request)
	return redirect(LOGOUT_REDIRECT_URL)
