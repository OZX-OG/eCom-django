from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json

def shop(request):
    context = {
        "products": Product.objects.all(),
        "categories": Categories.objects.all(),
    }
    return render(request, 'products/shop.html', context)

def single_product(request, slug):
    if request.method == "POST":
        if request.user.is_authenticated:
            new_quantity = int(request.POST.get("quantity"))

            if new_quantity > 0:

                customer = request.user.customer
                product = Product.objects.get(slug=slug)
                order, created = Order.objects.get_or_create(customer=customer, complete=False)
                orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
                orderItem.quantity = (orderItem.quantity + new_quantity)
                orderItem.save()
        else:
            pass


    context = {
            "products": Product.objects.all(),
            "product": Product.objects.get(slug=slug),
            "categories": Categories.objects.all(),
        }

    return render(request, 'products/single-Product.html', context)

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
    print("ana hna")
    if request.method == 'POST':
        username = request.POST.get("name")
        email = request.POST.get("email")
        city = request.POST.get("city")
        phone = request.POST.get("phone")

        print(username)
        print(city)
        print(city)
        print(phone)

        customer = request.user.customer
        print(customer)
        print(request.user)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        print(order)
        
        items = order.orderitem_set.all()
        print(items)

        order.complete = True
        order.save()

        # ShippingAddress.objects.create(
        #     customer = customer,
        #     order = order,
        #     name = "ozx",
        #     email = "fanpzx@gmail.com",
        #     city = "rabat",
        #     phone_number = "sala,"
        # )
        ShippingAddress.objects.create(
            customer = customer,
            order = order,
            name = username,
            email = email,
            city = city,
            phone_number = phone
        )
        return redirect('index')

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





def updateItem(request):
    data = json.loads(request.body)
    print(data)
    productSlug = data['productSlug']
    action = data['action']
    print('Action:', action)
    print('Product:', productSlug)

    customer = request.user.customer
    product = Product.objects.get(slug=productSlug)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

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
        print({
            'success': True,
            'product_total': int(product_total),
            'total_price': int(total_price),
        })
        return JsonResponse({
            'success': True,
            'product_total': int(product_total),
            'total_price': int(total_price),
        })
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