from django.forms import ModelForm
from core.models import Item

class AddItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'  # [takes in a list of fields to use]
        exclude = ['slug']
