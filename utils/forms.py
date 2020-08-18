from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django import forms

from core.models import UserProfile


class SignupForm(forms.ModelForm):
    retailer = forms.BooleanField(required=False)
    company = forms.CharField(max_length=50, required=False)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'company']

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        profile = UserProfile(user=user, is_retailer=self.cleaned_data['retailer'],
                              company_name=self.cleaned_data['company'])
        profile.save()
