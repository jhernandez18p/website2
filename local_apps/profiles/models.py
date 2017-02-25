import datetime
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.dispatch import receiver

from ckeditor.fields import RichTextField

from local_apps.iurd.models import Church


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



class UserProfile(models.Model):

    OBP = 1
    PR = 2
    PRAUX = 3
    OBR = 4
    PUEBLO = 5

    ROLE_CHOICES = (
        (OBR, 'Obispo'),
        (PR, 'Pastor'),
        (PRAUX, 'Pastor auxiliar'),
        (OBR, 'Obrero'),
        (PUEBLO, 'Pueblo'),
    )

    GENRE_CHOICE = (
        (1,('Hombre')),
        (2,('Mujer')),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    genre = models.IntegerField(choices=GENRE_CHOICE,default=1)
    bio = RichTextField()
    phone_regex = RegexValidator(regex=r'^\+?507?\d{8,15}$', message="Numero de telefono debe seguir este formato: '+999999999'.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15)
    avatar = models.ImageField(upload_to=upload_location, 
            null=True, 
            blank=True, 
            width_field="width_field", 
            height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    location = models.OneToOneField(Church, default=0, null=True, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    created = models.DateTimeField(auto_now=True,auto_now_add=False)
    time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)

    def user_name(self):
        return '%s %s' % (self.user.first_name, self.user.last_name,)

    def __str__(self):
        return self.user_name()

    class Meta:

        verbose_name = ('Perfil de usuario')
        verbose_name_plural = ('Perfil de usuarios')
        permissions = (
            ("can_create_user", "Puede crear usuarios"),
            ("can_delete_user", "Puede eliminar usuarios"),
            ("can_update_user", "Puede editar usuarios"),
        )

