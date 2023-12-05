from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import BrandProfile
from .models import  Merchandise, MerchandiseAvailableSizes


# If a new MErchandise is created, silmultaneously create a Sizes and Availble Sizes .. for the merch.


@receiver(post_save, sender=Merchandise)
def create_merchandise_sizes(sender, instance, created, **kwargs):
    if created:
 
        MerchandiseAvailableSizes.objects.create(sizes=instance)

        print("[NOTIFICATION] - Merchandise Size Created!")



