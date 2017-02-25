from settings.settings.base import LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode

from decouple import config
from .tokens import account_activation_token


def login(request):
	if request.user.is_authenticated():
		return redirect('/')
	elif request.method == 'GET':
		return render(request, 'auth/login.html',{'pg_title':'Iniciar Sesión'})
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
						'pg_title':'Iniciar Sesión',
					})
		else:
			return render(request, 'auth/login.html',{
							'warning': 'Usuario o contraseña erronea',
							'pg_title':'Iniciar Sesión',
							})


def register(request):
	""" #Funcion que permite registrar usuarios al sitio web """
	error_template = 'auth/register.html'
	if request.user.is_authenticated():
		return redirect('/')
	if request.method == 'POST' :

		username = request.POST['username']
		
		try:
			email = request.POST['email']
		except Exception as e:
			email = ''

		try:
			password1 = request.POST['password1']
			password2 = request.POST['password2']
		except Exception as e:
			password1 = ''
			password2 = ''

		if username == '':
			context = {
				'pg_title':'Error de Registro',
				'error':{
					'pg_title':'Nombre de usuario requerido!',
					'error':'show',
					'email':'El campo de correo no puede estar vacio, recuerde que debe terminar en "@universal.org.pa"',
					'contacto':'Por favor contactar al administrador de sistemas, info@universal.org.pa'
				}
			}
			return render(request,error_template,context)

		if email == '':
			context = {
				'pg_title':'Error de Registro',
				'error':{
					'pg_title':'Email requerido!',
					'error':'show',
					'email':'El campo de correo no puede estar vacio, recuerde que debe terminar en "@universal.org.pa"',
					'contacto':'Por favor contactar al administrador de sistemas, info@universal.org.pa'
				}
			}
			return render(request,error_template,context)

		if password1 != password2 or password2 == '' or password1 =='':
			context = {
				'pg_title':'Error de Registro',
				'error':{
					'pg_title':'Contraseña inconsistente',
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
		message = render_to_string('auth/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
		user.email_user(subject, message)
		context = {'pg_title':'registro completo'}
		return render(request,LOGIN_REDIRECT_URL,context)

	elif request.method == 'GET':

		template = 'auth/register.html'
		context ={
			'pg_title':'Registro',
			'error':{
				'error':'hide',
			}
		}
		return render(request, template, context)


def logout(request):

	auth.logout(request)
	return redirect(LOGOUT_REDIRECT_URL)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'auth/register.html')