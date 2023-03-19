from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['first_name', 'last_name', 'username', 'email', 'password']


admin.site.register(CustomUser)