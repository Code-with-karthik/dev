from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, user_email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not user_email:
            raise ValueError(_('The Email must be set'))
        user_email = self.normalize_email(user_email)
        user = self.model(user_email=user_email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, user_email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_active', True)

        return self.create_user(user_email, password, **extra_fields)