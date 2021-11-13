from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer
from .forms import CustomUserChangeForm,CustomUserCreationForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Customer
    fieldsets = (
        (None, {
            'fields': ('user_email', 'user_name', 'first_name', 'last_name', 'password')}
        ),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_email', 'user_name', 'first_name', 'last_name', 'password1', 'password2', )}
        ),
        ('Permissions', {
            'fields': ('is_staff', 'is_active')
        }),
    )
    list_display = ('user_email', 'is_staff', 'is_active',)
    list_filter = ('user_email', 'is_staff', 'is_active',)
    search_fields = ('user_email',)
    ordering = ('user_email',)


admin.site.register(Customer, CustomUserAdmin)