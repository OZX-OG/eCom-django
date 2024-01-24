from products.models import Order, OrderItem, ShippingAddress 


def order_info(request):
    orders = Order.objects.filter(complete = True).order_by('-date_order')
    client_info = ShippingAddress.objects.all().order_by('-date')
    products = []
    amounts = []

    for order in orders:
        order_items = OrderItem.objects.filter(order=order).order_by('-date_added')
        products.append(len(order_items))
        amo = 0
        for order_item in order_items:
            amo += order_item.get_total
        amounts.append(amo)

    return zip(client_info, products, amounts, orders)
    