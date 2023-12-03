from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import BrandProfile
from .models import  Merchandise, MerchandiseAvailableSizes


# If a new MErchandise is created, silmultaneously create a Sizes and Availble Sizes .. for the merch.


@receiver(post_save, sender=Merchandise)
def create_merhcandise_sizes(sender, instance, created, **kwargs):
    if created:
 
        MerchandiseAvailableSizes.objects.create(merchandise_name=instance)

        print("Brand Profile & Address Created!")

@receiver(post_save, sender=Merchandise)
def save_brand_profile(sender, instance, **kwargs):
    instance.size.save()
    instance.availble_size.save()
   
    print("Brand MerchandiseSizes saved!")
    print("Brand MerchandiseAvailableSizes!")
   

