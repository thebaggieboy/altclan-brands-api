from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets
from accounts.models import BrandProfile, BrandUser
from .models import  WishList, Merchandise, Leads, BrandDashboard, MerchandiseAvailableSizes, Aesthetics
from transactions.models import *

from .serializers import *
 
class MerchandiseViewSet(viewsets.ModelViewSet):
    queryset = Merchandise.objects.all().order_by('-date_created').values()
    serializer_class = MerchandiseSerializer
    #order_by = ['date_created']

class AestheticsViewSet(viewsets.ModelViewSet):
    queryset = Aesthetics.objects.all()
    serializer_class = AestheticsSerializer



class MerchandiseAvailableSizesViewSet(viewsets.ModelViewSet):
    queryset = MerchandiseAvailableSizes.objects.all()
    serializer_class = MerchandiseAvailableSizesSerializer

class LeadsViewSet(viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = BillingAddress.objects.all()
    serializer_class = AddressSerializer



class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer

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