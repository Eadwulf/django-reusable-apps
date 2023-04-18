from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

