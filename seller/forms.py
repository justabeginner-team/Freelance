from django import forms
from core.models import Item, ItemImage


class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'  # [takes in a list of fields to use]
        exclude = ['slug', 'user']


class ItemImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = ItemImage
        fields = ['image', ]
