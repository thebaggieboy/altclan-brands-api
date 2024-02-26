from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets
from .models import  Models

from .serializers import *
 
class ModelsViewSet(viewsets.ModelViewSet):
    queryset = Models.objects.all()
    serializer_class = ModelsSerializer


