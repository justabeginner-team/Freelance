from django.forms import ModelForm
from django import forms
from core.models import Item
from allauth.account.forms import SetPasswordField, PasswordField
from django.contrib.auth import get_user_model
from django.conf import settings


class AddItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'  # [takes in a list of fields to use]
        exclude = ['slug', 'user']

