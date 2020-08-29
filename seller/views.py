from django.template.loader import render_to_string
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.http.response import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.forms import modelformset_factory

from .forms import AddItemForm, ItemImageForm
from core.models import Item, ItemImage, Order, Rating
from core.filters import ItemFilter


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

# def mpesa(request):
#     response = lipa_na_mpesa_online(request, amount=1, phonenumber=254711521508)
#     return HttpResponse(response.text)


def admin(request):
    print(request.user)
    items_table = Item.objects.filter(user=request.user)
    recents = items_table.order_by('-created_on')[:3]

    obj = Order.objects.filter(items__item__user__exact=request.user)
    orders = obj.order_by('-start_date')[:3]

    rev = Rating.objects.filter(item__user=request.user).order_by('-created_on')
    print(obj.count())
    for k in obj:
        print(k.items)

    return render(request, 'admin-dash/index.html', {
        'items': items_table,
        'recents': recents,
        'orders': orders,
        'reviews': rev,
    })


# class AddItemFormView(FormView):
#     form_class = AddItemForm
#     template_name = 'add_item.html'
#
#     # success_url = 'seller:admin_view'
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.save()
#         messages.success(self.request,
#                          'Your Item has been added successfully')
#         return super(AddItemFormView, self).form_valid(form)
#
#     def get_success_url(self):  # overrides the actual method
#         return reverse('seller:admin_view')


def item_create(request):
    imageformset = modelformset_factory(ItemImage, form=ItemImageForm, extra=3)
    data = dict()
    if request.method == 'POST':
        itemForm = AddItemForm(request.POST, request.FILES)
        formset = imageformset(request.POST, request.FILES, queryset=ItemImage.objects.none())
        if itemForm.is_valid() and formset.is_valid():
            item_form = itemForm.save(commit=False)
            item_form.user = request.user
            item_form.save()
            for form in formset.cleaned_data:
                # this helps to not crash if the user
                # do not upload all the photos
                if form:
                    image = form['image']
                    photo = ItemImage(item=item_form, image=image)
                    photo.save()
            data['form_is_valid'] = True
            items_table = Item.objects.filter(user=request.user)
            data['html_item_list'] = render_to_string('admin-dash/partial_item_list.html', {
                'items': items_table,
            })
            messages.success(request,
                             ' Your product has been created successfully.')
        else:
            data['form_is_valid'] = False
            print(itemForm.errors, formset.errors)
    else:
        itemForm = AddItemForm()
        formset = imageformset(queryset=ItemImage.objects.none())

    context = {'form': itemForm, 'formset': formset}
    data['html_form'] = render_to_string('admin-dash/partial_item_create.html',
                                         context,
                                         request=request)

    return JsonResponse(data)


def update_item(request, slug):
    item = get_object_or_404(Item, slug=slug)
    imageformset = modelformset_factory(ItemImage, form=ItemImageForm, extra=3)
    data = dict()
    if request.method == 'POST':
        # this enables the form to be saved only in this instance
        form = AddItemForm(request.POST, request.FILES, instance=item)
        formset = imageformset(request.POST, request.FILES or None, instance=item)
        # not as a new form
        print(data)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            data['form_is_valid'] = True
            items_table = Item.objects.filter(user=request.user)
            data['html_item_list'] = render_to_string('admin-dash/partial_item_list.html', {
                'items': items_table,
            })
            messages.success(request,
                             ' Your product has been updated successfully.')
        else:
            data['form_is_valid'] = False
            print(form.errors, formset.errors)
    else:
        form = AddItemForm(request.POST or None, request.FILES or None, instance=item)
        formset = imageformset(queryset=ItemImage.objects.none(), instance=item)

    context = {'form': form,
               'formset': formset}
    data['html_form'] = render_to_string('admin-dash/partial_item_update.html',
                                         context,
                                         request=request)

    return JsonResponse(data)


def delete_item(request, slug):
    item = get_object_or_404(Item, slug=slug)
    data = dict()
    if request.method == 'POST':
        item.delete()
        data['form_is_valid'] = True
        items_table = Item.objects.filter(user=request.user)
        data['html_item_list'] = render_to_string('admin-dash/partial_item_list.html', {
            'items': items_table,
        })
        messages.success(request,
                         ' Your product has been deleted successfully.')

    else:
        context = {
            'item': item,
        }
        data['html_form'] = render_to_string('admin-dash/partial_item_delete.html',
                                             context,
                                             request=request
                                             )
    return JsonResponse(data)


# @require_GET
def retailer_dash(request):
    items = Item.objects.all().order_by('-created_on')[:3]
    orders = Order.objects.all()

    myfilter = ItemFilter(request.GET, queryset=items)
    items = myfilter.qs

    context_dict = {
        'items': items,
        'myfilter': myfilter,
        'orders': orders,

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


# your example view


def more_items(request):
    items = Item.objects.all()
    return render(request, "admin-dash/items.html", {'items': items, })


def more_orders(request):
    orders = Order.objects.all()
    return render(request, "admin-dash/orders.html", {'orders': orders, })
