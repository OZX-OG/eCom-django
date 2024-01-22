from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .forms import ShippingAddressForm
from .models import *
import json

def get_customer(request):
    try:
        customer = request.user.customer
    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)
    
    return customer

def shop(request):
    context = {
        "products": Product.objects.all(),
        "categories": Categories.objects.all(),
    }
    return render(request, 'products/shop.html', context)

def single_product(request, slug):
    if request.method == "POST":

        if request.POST.get("quantity") == "":
            new_quantity = 1
        else:
            new_quantity = int(float(request.POST.get("quantity")))

        if new_quantity > 0:
            customer = get_customer(request)

            product = Product.objects.get(slug=slug)
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
            orderItem.quantity = (orderItem.quantity + new_quantity)
            orderItem.save()

    context = {
            "products": Product.objects.all(),
            "product": Product.objects.get(slug=slug),
            "categories": Categories.objects.all(),
        }

    return render(request, 'products/single-Product.html', context)

def cart(request):
    customer = get_customer(request)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()

    context = {
        "items":items,
        "order":order,
    }
    return render(request, 'products/cart.html', context)

def checkout(request):
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            customer = get_customer(request)
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            
            items = order.orderitem_set.all()
            order.complete = True
            order.save()

            shipping_address = form.save(commit=False)
            shipping_address.customer = customer
            shipping_address.order = order
            shipping_address.save()

            messages.success(request, 'تم تقديم الطلبك بنجاح!')
        else:
            print("not valid")
            print(form.errors)
            messages.warning(request, 'Error in the form submission. Please check the errors above.')

    else:
        form = ShippingAddressForm()

    customer = get_customer(request)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()

    context = {
        'form': form,
        'items': items,
        'order': order,
    }

    return render(request, 'products/checkout.html', context)




def update_item(request):
    data = json.loads(request.body)
    print(data)
    productSlug = data['productSlug']
    print('Product:', productSlug)

    customer = get_customer(request)

    product = Product.objects.get(slug=productSlug)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    orderItem.quantity = (orderItem.quantity + 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    # Calculate the updated cart_items_count
    cart_items_count = order.orderitem_set.all()

    response_data = {
        'message': 'Item was added',
        'cart_items_count': len(cart_items_count),
    }
    return JsonResponse(response_data, safe=False)



def update_quantity(request, order_item_id, new_quantity):
    try:
        order_item = OrderItem.objects.get(pk=order_item_id)
        order_item.quantity = new_quantity
        order_item.save()

        # Recalculate updated product price, product total, and total price
        product_total = order_item.get_total
        total_price = order_item.order.get_cart_total
        response =  {
            'success': True,
            'product_total': int(product_total),
            'total_price': int(total_price),
        }

        print(response)
        return JsonResponse(response)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

def remove_item(request, order_item_id):
    try:
        order_item = OrderItem.objects.get(pk=order_item_id)
        order = order_item.order  # Retrieve the order before deletion

        # Remove the item
        order_item.delete()

        # Recalculate total price
        total_price = order.get_cart_total
        cartItems = OrderItem.objects.all()

        return JsonResponse({'success': True, 'total_price': total_price, 'cartItems': len(cartItems)})

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})