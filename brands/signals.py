from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import BrandProfile
from .models import  Merchandise, MerchandiseAvailableSizes


# If a new MErchandise is created, silmultaneously create a Sizes and Availble Sizes .. for the merch.


