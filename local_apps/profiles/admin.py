from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )
    list_select_related = ('userprofile', )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_location')
    
    def get_location(self, instance):
        return instance.userprofile.location
    get_location.short_description = 'location'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)



admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
