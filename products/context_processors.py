from .models import Order  # Import your model

def cart_items(request):
    items = []
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        print(len(items))
    return {'cartItems': len(items)}