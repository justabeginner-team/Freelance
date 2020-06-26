from django.urls import path
from .views import (
    add_item,
    delete_item,
    update_item,
    retailer_dash,
)

app_name='seller'

urlpatterns=[
    path('add_item/', add_item, name='add_item'),
    path('delete_item/<slug>', delete_item, name='delete_item'),
    path('update_item/<slug>', update_item, name='update_item'),
    path('retailer_dash/', retailer_dash, name='retailer_dash'),
]
