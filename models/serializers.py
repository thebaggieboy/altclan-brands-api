from rest_framework import serializers
from django.contrib.auth.models import User
from .models import  Models
from django.conf import settings
from accounts.models import BrandProfile



BrandUser = settings.AUTH_USER_MODEL



class ModelsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Models
        fields = ['model_name']

