from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ['user_email', 'title', 'text', 'date_posted']
