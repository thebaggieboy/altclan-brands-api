from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone
from brands.display import LABEL_DISPLAY, COLLECTION_DISPLAY, COMMUNITY_TYPE_DISPLAY
from brands.choices import STATUS, GENDER, COMMUNITY_TYPE, CLOTHING_CATEGORY
#from brands.models import Merchandise
from .choices import *
User = settings.AUTH_USER_MODEL

from django.contrib.postgres.fields import ArrayField
import uuid

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user



class BrandUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user



class CustomUser(AbstractBaseUser):
    
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    #user_type = models.CharField(choices=USER_TYPE, default='CustomUser', max_length=250)
    first_name = models.CharField(max_length=250, default='')
    last_name = models.CharField(max_length=250, default='')
    mobile_number = models.CharField(max_length=250, default='')
    display_picture = models.ImageField(upload_to='Display Picture', default='')  
    address = models.CharField(max_length=250, default='')
    city = models.CharField(max_length=250, default='')
    state = models.CharField(max_length=250, default='')
    zip = models.CharField(max_length=250, default='')
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email


    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    def has_perms(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    objects = UserManager()

class BrandUser(AbstractBaseUser):
    
    #username = models.CharField(blank=True, null=True, max_length=25, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    user_type = models.CharField(choices=USER_TYPE, max_length=250, default='brand' )
    brand_name = models.CharField(max_length=250, default='')
    brand_logo = models.URLField()
    brand_bio = models.TextField(default='')
    brand_type = models.CharField(choices=COMMUNITY_TYPE, default='', max_length=250)
    #followers = ArrayField(models.CharField(max_length=250),blank=True, null=True)
    mobile_number = models.CharField(max_length=250, default='')
    slug = models.SlugField(null=True, blank=True, default='')
    billing_address = models.CharField(max_length=250, default='')
    city = models.CharField(max_length=250, default='')
    state = models.CharField(max_length=250, default='')
    zip = models.CharField(max_length=250, default='')
    date_created = models.DateTimeField(default=timezone.now())

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email
    
    
    def get_username(self):
        # This user is identified by their username
        return self.username

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    def has_perms(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    objects = UserManager()




class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True, blank=True)
    #items = models.ManyToManyField()
    date_created = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return f'Profile :  {self.user}'

class BrandProfile(models.Model):
 
    user = models.OneToOneField(BrandUser, on_delete=models.CASCADE, related_name='brand_profile', null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now())

    
    def __str__(self):
        return f'{self.user} Profile'



class Followers(models.Model):
    user = models.OneToOneField(BrandUser, on_delete=models.CASCADE, related_name='brand_followers', null=True, blank=True)
     
    def __str__(self):
        return f'{self.user} Followers'