from django.shortcuts import render
from products.models import *

# # Create your views here.
def search(request):
    if request.method == 'GET':
        # Retrieve the search query entered by the user
        search_query = request.GET.get('q', '')
        # Filter your model by the search query
        products = Product.objects.filter(title__icontains=search_query)
        if search_query == '': 
            return {}
        else:
            return {'query':search_query, 'products':products}
        
def index(request):
    products = Product.objects.all()
    categories = Categories.objects.all()
    offers = Offer.objects.all()

    discounted_products = []  # List to store products with discounted prices

    for product in products:
        # Check if there is an associated offer for the product
        offer = offers.filter(product=product).first()

        if offer:
            # Calculate the discounted price
            discounted_price = product.price - (product.price * (offer.percentage / 100))
            
            # Create a dictionary with product details including the discounted price
            discounted_product_details = {
                'product': product,
                'discounted_price': discounted_price,
                'offer_percentage': offer.percentage,
            }

            discounted_products.append(discounted_product_details)
        else:
            # If no offer, use the original price
            discounted_products.append({'product': product, 'discounted_price': product.price, 'offer_percentage': 0})

    context = {
        "discounted_products": discounted_products,
        "categories": categories,
        "offers": offers,
    }

    return render(request, 'pages/index.html', context)


def return_policy(request):
    return render(request, 'pages/return-policy.html')

def error_404(request, exception):
    return render(request, 'pages/404.html')