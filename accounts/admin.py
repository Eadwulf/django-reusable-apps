from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(UserAdmin):
    model = User
    list_display = ['first_name', 'last_name', 'username', 'email', 'password']


admin.site.register(User)