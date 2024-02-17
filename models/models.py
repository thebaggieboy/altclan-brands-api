from django.db import models
import uuid
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.conf import settings
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Models(models.Model):
    model_name = models.CharField(max_length=250, null=True, blank=True)
    model_name = models.CharField(max_length=250, default='')

    model_description = models.TextField(default='')
    model_details = models.TextField(default='')
    model_gender = models.CharField( default='', null=True, blank=True, max_length=250)
    display_image = models.URLField()

  
    delivery_cost = models.FloatField(null=True, default=0.00)
 
    
    slug = models.SlugField()
    date_created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'Model Name : {self.model_name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.id}')
        return super().save(*args, **kwargs)