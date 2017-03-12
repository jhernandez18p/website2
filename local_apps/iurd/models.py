from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator, URLValidator
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.text import slugify

from ckeditor.fields import RichTextField


def upload_location(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
	PostModel = instance.__class__
	model_name = instance.__class__.__name__

	# model_name =
	try:
		_id = PostModel.objects.order_by("id").last().id
	except Exception as e:
		_id = 0
	new_id = _id + 1
	"""
    instance.__class__ gets the model Post. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object, 
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
	# print(instance.__class__.__name__)
	return "%s/%s/%s" %(model_name,new_id,filename)

class Category(models.Model):
	name = models.CharField(max_length=144)
	description = RichTextField()
	created = models.DateTimeField(auto_now=True,auto_now_add=False)
	time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-time_stamp','-updated']
		verbose_name = ('Nueva categoría')
		verbose_name_plural = ('Categorías')
		permissions = (
			("can_create_category", "Puede crear caregorías"),
			("can_delete_category", "Puede eliminar caregorías"),
			("can_update_category", "Puede editar caregorías"),
		)


class Church(models.Model):
	name = models.CharField(max_length=144)
	mail = models.EmailField(max_length=65)
	phone_regex = RegexValidator(regex=r'^\+?507?\d{8,15}$', message="Numero de telefono debe seguir este formato: '+999999999'.")
	telephone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15)
	image = models.ImageField(upload_to=upload_location, 
            null=True, 
            blank=True, 
            width_field="width_field", 
            height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	description = RichTextField()
	created = models.DateTimeField(auto_now=True,auto_now_add=False)
	time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-time_stamp','-updated']
		verbose_name = ('Iglesia')
		verbose_name_plural = ('Iglesias')
		permissions = (
			("can_create_church", "Puede crear iglesias"),
			("can_delete_church", "Puede eliminar iglesias"),
			("can_update_church", "Puede editar iglesias"),
		)


class Event(models.Model):
	name = models.CharField(max_length=144)
	title = models.CharField(max_length=144)
	description = RichTextField()
	mail = models.EmailField(max_length=65)
	start = models.DateTimeField(auto_now=False, auto_now_add=False)
	end = models.DateTimeField(auto_now=False, auto_now_add=False)
	created = models.DateTimeField(auto_now=True,auto_now_add=False)
	time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	church = models.ForeignKey(Church, default=1)
	location = RichTextField()
	category = models.ForeignKey(Category, null=True, blank=True)
	image = models.ImageField(upload_to=upload_location, 
            null=True, 
            blank=True, 
            width_field="width_field", 
            height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-time_stamp','-updated']
		verbose_name = ('Nuevo evento')
		verbose_name_plural = ('Enventos')
		permissions = (
			("can_create_event", "Puede crear eventos"),
			("can_delete_event", "Puede eliminar eventos"),
			("can_update_event", "Puede editar eventos"),
		)

	def get_absolute_url(self):
		return reverse("frontend:Event_detail", kwargs={"pk": self.id})


class Feed(models.Model):
	name = models.CharField(max_length=144)
	title = models.CharField(max_length=144)
	description = RichTextField()
	image = models.ImageField(upload_to=upload_location, 
        null=True, 
        blank=True, 
        width_field="width_field", 
        height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	url_feed = models.CharField(validators=[URLValidator()],max_length=144,blank=True)
	created = models.DateTimeField(auto_now=True,auto_now_add=False)
	time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-time_stamp','-updated']
		verbose_name = ('Nuevo Blog amigo')
		verbose_name_plural = ('Blogs amigos')
		permissions = (
			("can_create_feed", "Puede crear blog amigo"),
			("can_delete_feed", "Puede eliminar blog amigo"),
			("can_update_feed", "Puede editar blog amigo"),
		)


class Project(models.Model):
	GROUP = 'Groups'
	PROJECT = 'Projecs'

	CATEGORIES = (
		(GROUP,'Grupos'),
		(PROJECT,'Proyectos'),
	)

	name = models.CharField(max_length=144)
	title = models.CharField(max_length=144)
	slug = models.CharField(max_length=144)
	url = models.CharField(max_length=144)
	description = RichTextField()
	created = models.DateTimeField(auto_now=True,auto_now_add=False)
	time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	image = models.ImageField(upload_to=upload_location, 
            null=True, 
            blank=True, 
            width_field="width_field", 
            height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	background_image = models.ImageField(upload_to=upload_location, 
            null=True, 
            blank=True, 
            width_field="background_width_field", 
            height_field="background_height_field")
	background_height_field = models.IntegerField(default=0)
	background_width_field = models.IntegerField(default=0)
	project_type = models.CharField(max_length=10, choices=CATEGORIES)
	category = models.ForeignKey(Category, null=True, blank=True)
	parentId = models.ForeignKey("self", null=True, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-time_stamp','-updated']
		verbose_name = ('Nuevo Poyecto')
		verbose_name_plural = ('Proyectos')
		permissions = (
			("can_create_project", "Puede crear proyectos"),
			("can_delete_project", "Puede eliminar proyectos"),
			("can_update_project", "Puede editar proyectos"),
		)

	def get_absolute_url(self):
		return reverse("frontend:Project_detail", kwargs={"pk": self.id})


class Schedule(models.Model):
	name = models.CharField(max_length=144)
	description = RichTextField()
	start = models.TimeField(auto_now=False, auto_now_add=False)
	ends = models.TimeField(auto_now=False, auto_now_add=False)
	created = models.DateTimeField(auto_now=True,auto_now_add=False)
	time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['start','ends']
		verbose_name = ('Nuevo horario')
		verbose_name_plural = ('Horarios')
		permissions = (
			("can_create_schedule", "Puede crear horarios"),
			("can_delete_schedule", "Puede eliminar horarios"),
			("can_update_schedule", "Puede editar horarios"),
		)


class Reunion(models.Model):
	SUNDAY = 1
	MONDAY = 2
	TUESDAY = 3
	WEDNESDAY = 4
	THURSDAY = 5
	FRIDAY = 6
	SATURDAY = 7

	WEEKDAYS = (
		('0_MONDAY','Lunes'),
		('1_TUESDAY','Martes'),
		('2_WEDNESDAY','Miércoles'),
		('3_THURSDAY','Jueves'),
		('4_FRIDAY','Viernes'),
		('5_SATURDAY','Sábado'),
		('6_SUNDAY','Domingo'),
	)

	name = models.CharField(max_length=144)
	title = models.CharField(max_length=144)
	description = RichTextField()
	created = models.DateTimeField(auto_now=True,auto_now_add=False)
	time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	image = models.ImageField(upload_to=upload_location, 
            null=True, 
            blank=True, 
            width_field="width_field", 
            height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	background_image = models.ImageField(upload_to=upload_location, 
            null=True, 
            blank=True, 
            width_field="background_width_field", 
            height_field="background_height_field")
	background_height_field = models.IntegerField(default=0)
	background_width_field = models.IntegerField(default=0)
	category = models.CharField(max_length=20, choices=WEEKDAYS)
	parentId = models.ForeignKey("self",null=True, blank=True)
	schedule = models.ManyToManyField(Schedule)


	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-time_stamp','-updated']
		verbose_name = ('Nueva Reunion')
		verbose_name_plural = ('Reuniones')
		permissions = (
			("can_create_reunions", "Puede crear reuniones"),
			("can_delete_reunions", "Puede eliminar reuniones"),
			("can_update_reunions", "Puede editar reuniones"),
		)
	def get_absolute_url(self):
		return reverse("frontend:Reunions_detail", kwargs={"pk": self.id})


class Subscriber(models.Model):
	name = models.CharField(max_length=144)
	email = models.EmailField(max_length=65)
	phone = models.CharField(max_length=65, blank=True)
	description = RichTextField()
	created = models.DateTimeField(auto_now=True,auto_now_add=False)
	time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-time_stamp','-updated']
		verbose_name = ('Nuevo Suscriptor')
		verbose_name_plural = ('Suscriptores')
		permissions = (
			("can_create_subscribers", "Puede crear suscriptores"),
			("can_delete_subscribers", "Puede eliminar suscriptores"),
			("can_update_subscribers", "Puede editar suscriptores"),
		)
