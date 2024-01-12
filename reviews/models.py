from django.db import models
from django.shortcuts import reverse # Create your models here.
from django.conf import settings
from django.utils.text import slugify

from django.utils import timezone
User = settings.AUTH_USER_MODEL

# Create your models here.
class Reviews(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='reiews', null=True, blank=True)
    user_email =  models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField()
    review = models.TextField(default='', blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now())

    
    def get_absolute_url(self):
        return reverse('core:detail', kwargs={'slug':self.slug})

    def get_add_to_review_url(self):
        return reverse('review:add-to-review', kwargs={'slug':self.slug})

    def get_remove_from_review(self):
        return reverse('review:remove-from-review', kwargs={'slug':self.slug})

    def __str__(self):
        return f'{self.product}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.user}-review')
        return super().save(*args, **kwargs)
