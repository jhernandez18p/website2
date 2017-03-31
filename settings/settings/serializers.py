from django.contrib.auth.models import User, Group
from local_apps.iurd.models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ChurchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Church
        fields = (
            'id',
        	'name',
			'mail',
			'telephone_number',
			'image',
			'height_field',
			'width_field',
			'lat',
			'lng',
			'description',
        )