# -*- coding: utf-8 -*-
import operator,random,datetime
from local_apps.iurd.models import *
from local_apps.medias.models import *
from local_apps.news.models import *
from local_apps.testimonials.models import *


def cookies(request):
    site = {
        'name':'Iglesia Universal del Reino de Dios',
        'keywords':'iglesia universal panama pare de sufrir iurd iglesias cristianas fuerza jover jesuscristo',
        'description':'Iglesia Universal Panama, Sufre con problemas, ha intentado de todo y no sabe que más puede hacer. Visítenos en cualquier de nuestras Iglesias en todo el País ó escuche nuestra radio las 24 horas donde lo atenderemos.',
        'author':'Dev2tech',
    }
    now = datetime.datetime.now()
    context = {
        'time':now,
        'site':site,
    }
    context['redirect'] = True
    return context

def menu(request):
    context = {}
    WEEKDAYS = {
        '6_SUNDAY':{'id':1,'day':'Domingo','reunions':{}},
        '0_MONDAY':{'id':2,'day':'Lunes','reunions':{}},
        '1_TUESDAY':{'id':3,'day':'Martes','reunions':{}},
        '2_WEDNESDAY':{'id':4,'day':'Miércoles','reunions':{}},
        '3_THURSDAY':{'id':5,'day':'Jueves','reunions':{}},
        '4_FRIDAY':{'id':6,'day':'Viernes','reunions':{}},
        '5_SATURDAY':{'id':7,'day':'Sábado','reunions':{}},
    }
    reunions = Reunion.objects.all()
    for day in WEEKDAYS:
        for reunion in reunions:
            if reunion.category == day:
                WEEKDAYS[day]['reunions'][reunion.title]= {'name':reunion.title,'url':reunion.get_absolute_url}
    # print(WEEKDAYS)
    # WEEKDAYS.sort(key=operator.itemgetter('age'))
    context['weekdays'] = WEEKDAYS

    try:
        categories = Category.objects.all()
    except Exception as e:
        raise e
    context['site_categories'] = categories

    try:
        feeds = Feed.objects.all()
        context['feeds'] = feeds[:6]
    except Exception as e:
        print('No hay blogs amigos aún' + e)

    try:
        page_news = Post.objects.active().filter(draft=False)[:6]
        context['page_news'] = page_news
    except Exception as e:
        print(e)
        print('No hay noticias aún' + e)

    try:
        event = Event.objects.all().first()
        context['event'] = event
    except Exception as e:
        print(e)

    # try:
    #     session = request.session.get('user_rouge_for_pray', False)
    #     if request.session['user_rouge_for_pray'] == False:
    #         context['user_rouge_for_pray'] = False,
    #     else:
    #         context['user_rouge_for_pray'] = True
    # except Exception as e:
    #     print(e)

    try:
        page_events = Event.objects.all()
        context['page_events'] = page_events
    except Exception as e:
        print(e)
        raise e

    return context
