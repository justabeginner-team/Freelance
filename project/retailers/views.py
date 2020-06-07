from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def retailer(request):
    return HttpResponse('Retailer view')
