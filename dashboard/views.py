from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def todolist(request):
    return render(request, 'dashboard/todolist.html')

def order_details(request):
    return render(request, 'dashboard/order_details.html')

def all_order(request):
    return render(request, 'dashboard/all_orders.html')