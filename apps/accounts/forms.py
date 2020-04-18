from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.conf import settings

from apps.accounts.models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'phone_number')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'address', 'phone_number')

