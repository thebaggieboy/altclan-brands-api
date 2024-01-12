from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Reviews

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reviews
        fields = ['user_email', 'review', 'date_posted']
