# -*- coding: utf-8 -*-
import random,datetime
from local_apps.iurd.models import *
from local_apps.news.models import *

def cookies(request):

    now = datetime.datetime.now()

    context = {
        'time':now,
    }
    try:
        feeds = Feed.objects.all()
        context['feeds'] = feeds[:6]
    except Exception as e:
        print('No hay blogs amigos aún' + e)

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


    # print(request.session.get('user_rouge_for_pray'))
    if request.session.get('user_rouge_for_pray', False):
        context['user_rouge_for_pray'] = False,
    else:
        context['user_rouge_for_pray'] = True,

    return context

def menu(request):
    context = {}
    weekdays = ['domingo','lunes','martes','miercoles','jueves','viernes','sabado']
    context['weekdays'] = weekdays
    # Pages = Page.objects.all()

	# if Pages:
	# 	menu = [[x.title,x.slug] for x in Pages] 
	# 	print(nemu)

    return context