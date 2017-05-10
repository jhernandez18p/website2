from django.db import models
from django.core.validators import URLValidator
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.utils.text import slugify

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
	return "%s/%s/%s" %(model_name,new_id, filename)

class Testimonial(models.Model):
	title = models.CharField(max_length=144)
	slug = models.SlugField(max_length=140, blank=True)
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
	category = models.ForeignKey(Category, null=True, blank=True)

	def __str__(self):
		return self.slug

	def _get_unique_slug(self):
		slug = slugify(self.title)
		unique_slug = slug
		num = 1
		while Testimonial.objects.filter(slug=unique_slug).exists():
			unique_slug = '{}-{}'.format(slug, num)
			num += 1
		return unique_slug
 
	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = self._get_unique_slug()
		super().save()

	class Meta:
		ordering = ["-timestamp", "-updated"]
		verbose_name = ('Nuevo testimonio')
		verbose_name_plural = ('Testimonios')
		permissions = (
			("can_create_testimonial", "Puede crear testimonios"),
			("can_delete_testimonial", "Puede eliminar testimonios"),
			("can_update_testimonial", "Puede editar testimonios"),
	)

	def get_absolute_url(self):
		return reverse("frontend:Testimonial_detail", kwargs={"pk": self.slug})