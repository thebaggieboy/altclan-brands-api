from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


# Create your models here.
class Auctions(models.Model):
    product_name = models.CharField(max_length=250, null=True, blank=True)
    product_description = models.TextField(default='')
    display_image = models.URLField()
    highest_bid = models.CharField(max_length=250, null=True, blank=True)
    current_bid = models.CharField(max_length=250, null=True, blank=True)
    start_date = models.DateTimeField(default=timezone.now())
    end_date = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return f'{self.product_name} Auction'


    