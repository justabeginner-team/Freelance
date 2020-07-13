from requests.auth import HTTPBasicAuth
import requests
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.views.generic import FormView, View
from .decorators import retailer_required
from .forms import AddItemForm
from core.models import Item, Order, Rating
from core.filters import ItemFilter, CategoryFilter
from core.mixins import ProfileSignupView

from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# from webpush import send_user_notification
import json
from django.conf import settings


# Create your views here.

#
# def add_item(request):
#     form = AddItemForm()
#     if request.method == 'POST':
#         form = AddItemForm(request.POST, request.FILES)
#         if form.is_valid():
#             print('form is valid')
#             # user = request.user
#             # obj = Item(user=user)
#             # obj.save()
#             form.save()
#             messages.success(request,
#                              ' Your product has been added successfully.')
#             return redirect('seller:admin_view')
#     context_dict = {
#         'form': form,
#     }
#     return render(request, 'add_item.html', context=context_dict)


class AddItemFormView(FormView):
    form_class = AddItemForm
    template_name = 'add_item.html'

    # success_url = 'seller:admin_view'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        messages.success(self.request,
                         'Your Item has been added successfully')
        return super(AddItemFormView, self).form_valid(form)

    def get_success_url(self):  # overrides the actual method
        return reverse('seller:admin_view')


def delete_item(request, slug):
    item = Item.objects.get(slug=slug)
    if request.method == 'POST':
        item.delete()
        messages.success(request,
                         ' Your product has been deleted successfully.')
        return redirect('seller:admin_view')
    context_dict = {
        'item': item,
    }
    return render(request, 'delete_item.html', context=context_dict)


def update_item(request, slug):
    item = Item.objects.get(slug=slug)
    form = AddItemForm(instance=item)  # prefills the form to be updated
    if request.method == 'POST':
        # this enables the form to be saved only in this instance
        form = AddItemForm(request.POST, instance=item)
        # not as a new form
        if form.is_valid():
            form.save()
            messages.success(request,
                             ' Your product has been updated successfully.')
            return redirect('seller:admin_view')
    context_dict = {
        'form': form,
    }
    return render(request, 'add_item.html', context=context_dict)


# @require_GET
def retailer_dash(request):
    items = Item.objects.all()
    orders = Order.objects.all()

    myfilter = ItemFilter(request.GET, queryset=items)
    items = myfilter.qs

    # webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
    # vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
    # user = request.user

    context_dict = {
        'items': items,
        'myfilter': myfilter,
        'orders': orders,
        #   'user': user,
        #   'vapid_key': vapid_key
    }
    return render(request, 'retailer_dash.html', context=context_dict)


# @require_POST
# @csrf_exempt
# def send_push(request):
#     try:
#         body = request.body
#         data = json.loads(body)
#
#         if 'head' not in data or 'body' not in data or 'id' not in data:
#             return JsonResponse(status=400, data={"message": "Invalid data format"})
#
#         user_id = data['id']
#         user = get_object_or_404(User, pk=user_id)
#         payload = {'head': data['head'], 'body': data['body']}
#         send_user_notification(user=user, payload=payload, ttl=1000)
#
#         return JsonResponse(status=200, data={"message": "Web push successful"})
#     except TypeError:
#         return JsonResponse(status=500, data={"message": "An error occurred"})


def admin(request):
    items_table = Item.objects.filter(user=request.user)
    recents = items_table.order_by('-created_on')[:3]
    obj = Order.objects.filter(items__item__user__exact=request.user)
    orders = obj.order_by('-start_date')
    rev = Rating.objects.filter(item__user=request.user).order_by('-created_on')
    return render(request, 'admin-dash/index.html', {
        'items': items_table,
        'recents': recents,
        'orders': orders,
        'reviews': rev,
    })

# your example view
