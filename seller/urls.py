from django.views.generic import TemplateView
from django.urls import path
from .views import (
    # add_item,
    item_create,
    delete_item,
    update_item,
    # retailer_dash,
    # RetailerSignupView
    # send_push,
    admin,
    mpesa,

)

app_name = 'seller'

urlpatterns = [
    # path('add_item/', AddItemFormView.as_view(), name='add_item'),
    path('create_item/', item_create, name='add_item'),
    path('update_item/<slug>', update_item, name='update_item'),
    path('delete_item/<slug>', delete_item, name='delete_item'),
    path('template/', admin, name='admin_view'),
    path('mpesa/', mpesa),
]
