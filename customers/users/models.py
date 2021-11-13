from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from .managers import CustomUserManager
# Create your models here.

class Customer(AbstractBaseUser, PermissionsMixin):
    user_name   = models.CharField(max_length=200)
    user_email  = models.EmailField(max_length=70, unique=True)
    first_name  = models.CharField(max_length=200)
    last_name   = models.CharField(max_length=300)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.user_name