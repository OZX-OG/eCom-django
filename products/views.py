from django.shortcuts import render
from .models import *

def shop(request):
    context = {
        "products": product.objects.all(),
        "categories": Categories.objects.all(),
    }
    return render(request, 'products/shop.html', context)

def single_product(request, slug):
    context = {
            "products": product.objects.all(),
            "product": product.objects.get(slug=slug),
            "categories": Categories.objects.all(),
        }

    return render(request, 'products/single-product.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {}

    context = {
        "items":items,
        "order":order,
    }
    return render(request, 'products/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {}

    context = {
        "items":items,
        "order":order,
    }

    return render(request, 'products/checkout.html', context)