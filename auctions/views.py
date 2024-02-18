from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets
from .models import  Auctions


from .serializers import *
 
class MerchandiseViewSet(viewsets.ModelViewSet):
    queryset = Auctions.objects.all()
    serializer_class = Mer
    


