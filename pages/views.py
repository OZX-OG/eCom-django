from django.shortcuts import render
from products.models import *

# # Create your views here.
def index(request):
    context = {
        "products": product.objects.all(),
        "categories": Categories.objects.all(),
    }
    return render(request, 'pages/index.html', context)



def return_policy(request):
    return render(request, 'pages/return-policy.html')