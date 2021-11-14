from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from .models import Customer
from django import forms

class CustomUserCreationForm(UserCreationForm):
    """
    A form for creating new users. Includes all the required fields, plus a repeated password.
    """
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = Customer
        fields = ('user_email', 'password1', 'password2', )

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Customer
        fields = ('user_email', 'password',  )
