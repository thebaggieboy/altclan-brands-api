from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets
from accounts.models import BrandProfile, BrandUser
from .models import  Cart, Merchandise, Leads, BrandDashboard, MerchandiseAvailableSizes
from transactions.models import *

from .serializers import *
 
class MerchandiseViewSet(viewsets.ModelViewSet):
    queryset = Merchandise.objects.all()
    serializer_class = MerchandiseSerializer

class MerchandiseAvailableSizesViewSet(viewsets.ModelViewSet):
    queryset = MerchandiseAvailableSizes.objects.all()
    serializer_class = MerchandiseAvailableSizesSerializer

class LeadsViewSet(viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = BillingAddress.objects.all()
    serializer_class = AddressSerializer



class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

# Create your views here.
class BrandDashboardViewSet(viewsets.ModelViewSet):
    queryset = BrandDashboard.objects.all()
    serializer_class = BrandDashboardSerializer

# Create your views here.
class BrandProfileViewSet(viewsets.ModelViewSet):
    queryset = BrandProfile.objects.all()
    serializer_class = BrandProfileSerializer




def create_merchandise_list(request):

    return render(request, 'alteclan/index.html')