from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
# Create your models here.

class Customer(AbstractBaseUser, PermissionsMixin):
    user_name    = models.CharField(max_length=200)
    user_email   = models.EmailField(max_length=70, unique=True)
    first_name   = models.CharField(max_length=200)
    last_name    = models.CharField(max_length=300)
    date_joined  = models.DateTimeField(default=timezone.now)
    is_active    = models.BooleanField(default=True)
    is_staff     = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.user_email

class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class Orders(models.Model):
    Customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
    Product = models.ForeignKey('Products', on_delete=models.CASCADE)
    Quantity = models.IntegerField()

    def __str__(self) -> str:
        return str(self.Customer_id)