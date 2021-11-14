from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
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
    
    # This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)