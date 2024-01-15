from django.shortcuts import render
from .models import *

def shop(request):
    return render(request, 'products/shop.html')

def single_product(request, slug):
    context = {
            "products": product.objects.all(),
            "product": product.objects.get(slug=slug),
            "categories": Categories.objects.all()
        }

    return render(request, 'products/single-product.html', context)

def cart(request):
    return render(request, 'products/cart.html')

def checkout(request):
    return render(request, 'products/checkout.html')