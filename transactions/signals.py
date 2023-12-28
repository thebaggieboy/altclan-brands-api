from django.db.models.signals import post_save
from django.dispatch import receiver

from transactions.models import Payment, Order


# If a new MErchandise is created, silmultaneously create a Sizes and Availble Sizes .. for the merch.

# If a new brand is created, silmultaneously create a profile & dashboard for the brand.
@receiver(post_save, sender=Payment)
def create_transaction_order(sender, instance, created, **kwargs):
    if created:
        Order.objects.create(user=instance)
    
        print("[SIGNALS] Payment Order Created!")

@receiver(post_save, sender=Payment)
def save_transaction_order(sender, instance, **kwargs):
    instance.user_order.save()
 
    print("[SIGNALS] Payment Order Saved!")
   
   
