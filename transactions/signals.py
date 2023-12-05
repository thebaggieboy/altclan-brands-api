from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import  Payment, Order


# If a new Payment is created, silmultaneously create an order with that payment.


