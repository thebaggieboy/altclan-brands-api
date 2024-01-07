from django.db import models

# Create your models here.
from django.utils import timezone
from django.template.defaultfilters import slugify



# Create your models here.
class Communities(models.Model):
    community_name = models.CharField(max_length=250, null=True, blank=True)
    community_type = models.CharField(max_length=250, null=True, blank=True)
    community_description = models.TextField(default='')
    display_image = models.URLField()
    
    def __str__(self):
        return f'{self.product_name} Auction'