from django.views.generic import TemplateView
from django.urls import path
from .views import (
    add_item,
    delete_item,
    update_item,
    retailer_dash,
    # RetailerSignupView
    # send_push,
    admin,
)

app_name = 'seller'

urlpatterns = [
    path('add_item/', add_item, name='add_item'),
    path('delete_item/<slug>', delete_item, name='delete_item'),
    path('update_item/<slug>', update_item, name='update_item'),
    path('retailer_dash/', retailer_dash, name='retailer_dash'),
    # path('ret/',RetailerSignupView.as_view()),
    # path('send_push', send_push),
    # path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript')),
    path('template/', admin, name='admin_view')
]
