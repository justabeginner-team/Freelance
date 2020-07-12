
from django import forms
from django.forms import ModelForm
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import Item, Rating,UserProfile
from allauth.account.adapter import DefaultAccountAdapter, get_adapter
from django.contrib.auth import get_user_model
from allauth.account.forms import SetPasswordField, PasswordField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.conf import settings
from django.contrib.auth import get_user_model



PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal'),
    ('M','Mpesa')
)


class SignupForm(forms.ModelForm):
    retailer=forms.BooleanField(required=False)
    company = forms.CharField(max_length=50)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'company']

    def signup(self, request, user):

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        profile = UserProfile(user=user,is_retailer=self.cleaned_data['retailer'],
                              company_name=self.cleaned_data['company'])
        profile.save()


class CheckoutForm(forms.Form):
    phonenumber = forms.CharField(required=False)
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    shipping_zip = forms.CharField(required=False)

    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    billing_zip = forms.CharField(required=False)

    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()


class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)


class AddReviewForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['subject', 'review', 'rate']
