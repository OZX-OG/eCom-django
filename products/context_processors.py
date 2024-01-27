from .models import Order, Customer

def cart_items(request):
    items = []
    try:
        customer = request.user.customer
    except AttributeError :

        try:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
        except: 
            items = []


    return {'cartItems': len(items),} 

def crsf_token(request):
    csrf_token_included = request.session.get('csrf_token_included', False)

    # Update the flag in the session
    request.session['csrf_token_included'] = True

    return {'csrf_token_included': csrf_token_included}