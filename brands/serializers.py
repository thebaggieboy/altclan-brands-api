from rest_framework import serializers
from django.contrib.auth.models import User
from .models import  Merchandise, Cart, Leads, BrandDashboard, BillingAddress, MerchandiseAvailableSizes, Aesthetics
from django.conf import settings
from accounts.models import BrandProfile



BrandUser = settings.AUTH_USER_MODEL



class BrandProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BrandProfile
        fields = ['id','user','date_created']

class BrandDashboardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BrandDashboard
        fields = ['user', 'total_views', 'items', 'total_products', 'total_users', 'total_profit']



class LeadsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Leads
        fields = ['id','brand_name', 'instagram_username', 'website_link']

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BillingAddress
        fields = ['user','street_address', 'city', 'state', 'zip']



class MerchandiseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Merchandise
        fields = [
            'id','brand_name', 'merchandise_name', 'size_type',  'merchandise_gender', 'available_sizes', 'available_colors', 'merchandise_type', 'labels', 'delivery_cost',  'merchandise_description', 'merchandise_details', 'price', 'display_image',
        ]
        
        
class AestheticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aesthetics
        fields = [
            'id','aesthetic_name', 'aesthetic_image'
        ]
        
             
class MerchandiseAvailableSizesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MerchandiseAvailableSizes
        fields = [
             'sizes',
        ]
        


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','quantity', 'merchandises']
