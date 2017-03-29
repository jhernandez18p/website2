from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator
from django.core.validators import URLValidator

from local_apps.iurd.models import Category
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


class Newspaper(models.Model):
	title = models.CharField(max_length=144)
	edition = models.PositiveIntegerField(validators=[MaxValueValidator(1000),])
	description = RichTextField()
	image = models.ImageField(upload_to=upload_location, 
	null=True, 
	blank=True, 
	width_field="width_field", 
	height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	newspaper_file = models.FileField(upload_to=upload_location,blank=True)
	newspaper_url = models.CharField(validators=[URLValidator()],max_length=144,blank=True)
	active = models.BooleanField(default=True)
	publish = models.DateField(auto_now=False, auto_now_add=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-timestamp", "-updated"]
		verbose_name = ('Nuevo Periodico')
		verbose_name_plural = ('Periodicos')
		permissions = (
			("can_create_newspaper", "Puede crear periodicos"),
			("can_delete_newspaper", "Puede eliminar periodicos"),
			("can_update_newspaper", "Puede editar periodicos"),
		)

	def get_absolute_url(self):
		return reverse("frontend:Newspaper", kwargs={"id": self.id})

class Video(models.Model):
	title = models.CharField(max_length=144)
	description = RichTextField()
	image = models.ImageField(upload_to=upload_location, 
	null=True, 
	blank=True, 
	width_field="width_field", 
	height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	video_url = models.CharField(max_length=144,blank=True)
	video_file = models.FileField(upload_to=upload_location,blank=True)
	active = models.BooleanField(default=True)
	publish = models.DateField(auto_now=False, auto_now_add=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	category = models.ForeignKey(Category, null=True, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-timestamp", "-updated"]
		verbose_name = ('Nuevo video')
		verbose_name_plural = ('Videos')
		permissions = (
			("can_create_video", "Puede crear video"),
			("can_delete_video", "Puede eliminar video"),
			("can_update_video", "Puede editar video"),
		)


class Tv(models.Model):
	title = models.CharField(max_length=144)
	description = RichTextField()
	image = models.ImageField(
		upload_to=upload_location, 
		null=True, 
		blank=True, 
		width_field="width_field", 
		height_field="height_field"
	)
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	video_url = models.CharField(validators=[URLValidator()],max_length=144,blank=True)
	video_file = models.FileField(upload_to=upload_location,blank=True)
	active = models.BooleanField(default=True)
	publish = models.DateField(auto_now=False, auto_now_add=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	category = models.ForeignKey(Category, null=True, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-timestamp", "-updated"]
		verbose_name = ('Tv')
		verbose_name_plural = ('Tv')
		permissions = (
			("can_create_tv", "Puede crear tv"),
			("can_delete_tv", "Puede eliminar tv"),
			("can_update_tv", "Puede editar tv"),
		)

class Audio(models.Model):
	title = models.CharField(max_length=144)
	description = RichTextField()
	image = models.ImageField(upload_to=upload_location, 
	null=True, 
	blank=True, 
	width_field="width_field", 
	height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	audio_url = models.CharField(validators=[URLValidator()],max_length=144,blank=True)
	audio_file = models.FileField(upload_to=upload_location,blank=True)
	active = models.BooleanField(default=True)
	publish = models.DateField(auto_now=False, auto_now_add=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	category = models.ForeignKey(Category, null=True, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-timestamp", "-updated"]
		verbose_name = ('Nuevo audio')
		verbose_name_plural = ('Audios')
		permissions = (
			("can_create_audio", "Puede crear audios"),
			("can_delete_audio", "Puede eliminar audios"),
			("can_update_audio", "Puede editar audios"),
		)


class Image(models.Model):
	title = models.CharField(max_length=144)
	description = RichTextField()
	image = models.ImageField(upload_to=upload_location, 
	null=True, 
	blank=True, 
	width_field="width_field", 
	height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	image_url = models.CharField(validators=[URLValidator()],max_length=144,blank=True)
	active = models.BooleanField(default=True)
	publish = models.DateField(auto_now=False, auto_now_add=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	category = models.ForeignKey(Category, null=True, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-timestamp", "-updated"]
		verbose_name = ('Nueva imagen')
		verbose_name_plural = ('Imagenes')
		permissions = (
			("can_create_image", "Puede crear imagenes"),
			("can_delete_image", "Puede eliminar imagenes"),
			("can_update_image", "Puede editar imagenes"),
		)


class Radio(models.Model):
	title = models.CharField(max_length=144)
	description = RichTextField()
	image = models.ImageField(
		upload_to=upload_location, 
		null=True, 
		blank=True, 
		width_field="width_field", 
		height_field="height_field"
	)
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	audio_url = models.CharField(validators=[URLValidator()],max_length=144,blank=True)
	audio_file = models.FileField(upload_to=upload_location,blank=True)
	active = models.BooleanField(default=True)
	publish = models.DateField(auto_now=False, auto_now_add=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	category = models.ForeignKey(Category, null=True, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-timestamp", "-updated"]
		verbose_name = ('Radio')
		verbose_name_plural = ('Radio')
		permissions = (
			("can_create_radio", "Puede crear radio"),
			("can_delete_radio", "Puede eliminar radio"),
			("can_update_radio", "Puede editar radio"),
		)
		
