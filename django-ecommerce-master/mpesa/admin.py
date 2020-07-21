from django.contrib import admin
from .models import MpesaCallBacks,MpesaCalls,MpesaPayment
# Register your models here.

admin.site.register(MpesaPayment)
admin.site.register(MpesaCallBacks)
admin.site.register(MpesaCalls)