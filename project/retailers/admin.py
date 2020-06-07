from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Retailer)
admin.site.register(Product)
admin.site.register(Order)

