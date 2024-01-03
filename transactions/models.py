from django.db import models
from django.conf import settings
import uuid
from django.utils import timezone
from django.utils.crypto import get_random_string
from brands.models import BillingAddress
from django.utils.text import slugify
from django.conf import settings

User = settings.AUTH_USER_MODEL
RANDOM_ORDER_ID = get_random_string(length=8)

STATUS = (
    ('P', 'Pending'),
    ('C', 'Completed'),
)

# Create your models here.
class Order(models.Model): 


    name_of_item = models.CharField(max_length=250, blank=True)
    user_email = models.CharField(max_length=250, blank=True)
    name_of_brand = models.CharField(max_length=250, blank=True)
    amount_per_item = models.CharField(max_length=250, blank=True)
    quantity = models.CharField(max_length=250, blank=True)
    tracking_number = models.CharField(max_length=250, default=get_random_string(length=12))
    number_of_items = models.IntegerField(null=True)
    address = models.CharField(max_length=250, blank=True)
    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    order_date = models.DateTimeField(default=timezone.now())
    

    def __str__(self):
        return f'{self.tracking_number}'


class Payment(models.Model):
    #id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, )
    user_email = models.CharField(max_length=250, blank=True)
    full_name = models.CharField(max_length=250, blank=True)
    paystack_charge_id = models.CharField(max_length=50, default='', null=True, blank=True)
    amount = models.FloatField()
    status = models.CharField(max_length=250, choices=STATUS, null=True, blank=True)
    #order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.amount


class Coupon(models.Model):
    #id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code


class Refund(models.Model):
    #id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.reason}"