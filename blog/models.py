from django.db import models
from django.shortcuts import reverse # Create your models here.
from django.conf import settings
from django.utils.text import slugify

from django.utils import timezone
User = settings.AUTH_USER_MODEL

# Create your models here.
class Blog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='blog', null=True, blank=True)
    user_email =  models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField()
    title = models.CharField(max_length=250, null=True, blank=True)
    text = models.TextField(default='', blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now())



    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.user}-review')
        return super().save(*args, **kwargs)
