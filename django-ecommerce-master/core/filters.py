import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class ItemFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name='date_created', lookup_expr='gte') # gte --> greater than or equal to
    # end_date = DateFilter(field_name='date_created', lookup_expr='lte')  # lte --> less than or equal to
    description = CharFilter(field_name='description',
                             lookup_expr='icontains')  # icontains means ignore case sensitivity

    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['slug', 'image', 'date_created']
