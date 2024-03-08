
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework import viewsets
from .serializers import UserSerializer, ProfileSerializer, BrandUserSerializer
from brands.serializers import BrandDashboardSerializer, BrandProfileSerializer
from .models import Profile, CustomUser, BrandUser, BrandProfile
from brands.models import BrandDashboard
from django.conf import settings
#BrandUser = settings.BRAND_USER_MODEL

class GoogleLogin(SocialLoginView): # if you want to use Implicit Grant, use this
    adapter_class = GoogleOAuth2Adapter


    

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = BrandProfile.objects.all()
    serializer_class = BrandProfileSerializer

class BrandUserViewSet(viewsets.ModelViewSet):
    queryset = BrandUser.objects.all().order_by('-date_created').values()
    serializer_class = BrandUserSerializer

class BrandDashboardViewSet(viewsets.ModelViewSet):
    queryset = BrandDashboard.objects.all()
    serializer_class = BrandDashboardSerializer
    
    


"""class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = CALLBACK_URL_YOU_SET_ON_GOOGLE
    client_class = OAuth2Client
"""

