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
from local_apps.iurd.models import (Project)
from local_apps.medias.models import (Image,Video)
from local_apps.news.models import (Post)

# class Slide(models.Model):
#     """# Media Widget """
#     MEDIA_TYPE = (
#         ('image', 'Imagenes'),
#         ('video', 'Videos'),
#     )
#     PARENT_TYPE = (
#         ('post','Noticias'),
#         ('group','Proyectos'),
#     )
#     SITE_POSITION = (
#         ('1','Inicio'),
#         ('2','Detalles'),
#     )

#     name = models.CharField(max_length=144)
#     title = RichTextField(blank=True)
#     site_position = models.CharField(max_length=10, choices=SITE_POSITION)
#     parent_type = models.CharField(max_length=10, choices=PARENT_TYPE)
#     related_post = models.ForeignKey(Post, blank=True, related_name='slide_related_post')
#     related_project = models.ForeignKey(Project, blank=True, related_name='slide_related_project')
#     media_type = models.CharField(max_length=10, choices=MEDIA_TYPE)
#     related_image = models.ManyToManyField(Image, blank=True, related_name='slide_related_image')
#     related_video = models.ManyToManyField(Video, blank=True, related_name='slide_related_video')
#     created = models.DateTimeField(auto_now=True,auto_now_add=False)
#     timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True, auto_now_add=False)

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ["-timestamp", "-updated"]
#         verbose_name = ('Carrusel')
#         verbose_name_plural = ('Carrusel')
#         permissions = (
#             ("can_create_slide", "Puede crear slide"),
#             ("can_delete_slide", "Puede eliminar slide"),
#             ("can_update_slide", "Puede editar slide"),
#         )