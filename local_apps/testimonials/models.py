from django.db import models
from django.core.validators import URLValidator

from ckeditor.fields import RichTextField
# Create your models here.

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
	return "%s/%s/%s" %(model_name,new_id, filename)


class Testimonial(models.Model):
	title = models.CharField(max_length=144)
	publisher = models.CharField(max_length=144, default='User')
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

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-timestamp", "-updated"]
		verbose_name = ('Nuevo testimonio')
		verbose_name_plural = ('Testimonios')
		permissions = (
			("can_create_testimonial", "Puede crear testimonios"),
			("can_delete_testimonial", "Puede eliminar testimonios"),
			("can_update_testimonial", "Puede editar testimonios"),
	)