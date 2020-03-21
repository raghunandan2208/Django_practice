from django.shortcuts import render
from django.http import HttpResponse
from products.models import Item
from products.models import Category
# Create your views here.

def display(request):
    categories = Category.objects.all()
    context = {
    'categories' : categories,
    }
    return render(request, 'products/base.html', context)

def index(request, *args, **kwargs):
    items = Item.objects.filter(p_status = "A")
    context = {
    'items' : items,
    }
    return render(request, 'products/products.html', context)

def category_buttons(request, id, *args, **kwargs):
    items = Item.objects.filter(category__id = id)
    context = {
    'items' : items,
    }
    return render(request, 'products/products.html', context)

def details_page(request, id, *args, **kwargs):
    try:
        item = Item.objects.get(id = id)
        similar = Item.objects.filter(p_title__icontains=item)
        context = {
        'item' : item,
        'similar' : similar,
        }
        return render(request, 'products/details.html', context)
    except:
        return HttpResponse("Invalid ID")
