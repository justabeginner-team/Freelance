from django.shortcuts import render, redirect
from .decorators import retailer_required
from .forms import AddItemForm
from core.models import Item, Order
from core.filters import ItemFilter, CategoryFilter


# Create your views here.


def add_item(request):
    form = AddItemForm()
    if request.method == 'POST':
        form = AddItemForm(request.POST, request.FILES)
        if form.is_valid():
            print('form is valid')
            form.save()
            return redirect('core:retailer_dash')
    context_dict = {
        'form': form,
    }
    return render(request, 'add_item.html', context=context_dict)


@retailer_required
def delete_item(request, slug):
    item = Item.objects.get(slug=slug)
    if request.method == 'POST':
        item.delete()
        return redirect('seller:retailer_dash')
    context_dict = {
        'item': item,
    }
    return render(request, 'delete_item.html', context=context_dict)


@retailer_required
def update_item(request, slug):
    item = Item.objects.get(slug=slug)
    form = AddItemForm(instance=item)  # prefills the form to be updated
    if request.method == 'POST':
        # this enables the form to be saved only in this instance
        form = AddItemForm(request.POST, instance=item)
        # not as a new form
        if form.is_valid():
            form.save()
            return redirect('seller:retailer_dash')
    context_dict = {
        'form': form,
    }
    return render(request, 'add_item.html', context=context_dict)


def retailer_dash(request):
    items = Item.objects.all()
    orders = Order.objects.all()

    myfilter = ItemFilter(request.GET, queryset=items)
    items = myfilter.qs

    context_dict = {
        'items': items,
        'myfilter': myfilter,
        'orders': orders,
    }
    return render(request, 'retailer_dash.html', context=context_dict)
