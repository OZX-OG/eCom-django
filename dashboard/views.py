from django.shortcuts import render, redirect, get_object_or_404
from products.models import *
from .models import Task
from .forms import OrderStatusForm, TaskForm
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.contrib import messages
from .utils import order_info
from django.http import JsonResponse

# Create your views here.
def index(request):
    today = datetime.now().date()
    today_sale = sum(order.get_cart_total for order in Order.objects.filter(date_order__date=today, complete=True))
    today_order_count = Order.objects.filter(date_order__date=today, complete=True).count()

    total_sale = sum(order.get_cart_total for order in Order.objects.filter(complete = True))
    total_order_count = Order.objects.filter(complete=True).count()

    context = {
        'order_infos': order_info(request),
     
        'today_sale': today_sale,
        'total_sale': total_sale,
        'today_order_count': today_order_count,
        'total_order_count': total_order_count,
    
        'tasks': Task.objects.filter(user=request.user),
    }
    return render(request, 'dashboard/index.html', context)

def all_order(request):
    context = {
        'order_infos': order_info(request),
    }

    return render(request, 'dashboard/all_orders.html', context)

def order_details(request, pk):
    orderitems = OrderItem.objects.filter(order=pk)
    client_info = ShippingAddress.objects.get(order=pk)

    if request.method.lower() == 'post':
        form = OrderStatusForm(request.POST)
        if form.is_valid():
            selected_status = form.cleaned_data['status']

            client_info.status = selected_status
            client_info.save()

    else:
        form = OrderStatusForm()

    quantity = sum([ x.quantity for x in orderitems ])
    total_price = sum([ x.get_total for x in orderitems ])

    context = {
        "orderitems": orderitems,
        "client_info": client_info,
        'form': form,
        "total": {
                'all_items': len(orderitems),
                'quantity': quantity,
                'total_price': total_price,
            },
    }
    return render(request, 'dashboard/order_details.html', context)

def signin(request):
    if request.method.upper() == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
      
        user = authenticate(request, username=username, password=password)
      
        if user is not None:
            login(request, user)
            return redirect('dash_index')
        else: 
            messages.warning(request, 'Username OR Password is incorrect')

    return render(request, 'dashboard/signin.html')

def logoutUser(request):
    logout(request)
    return redirect("index")



def todolist(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'dashboard/todolist.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            task = Task.objects.create(title=title, user=request.user)
            return JsonResponse({'message': 'Task added successfully.', 'task_id': task.id}, status=200)
        else:
            return JsonResponse({'error': 'Title cannot be empty.'}, status=400)

    return render(request, 'todo_app/add_task.html')

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            task.title = title
            task.save()
            return JsonResponse({'message': 'Task updated successfully.'}, status=200)
        else:
            return JsonResponse({'error': 'Title cannot be empty.'}, status=400)

    return render(request, 'todo_app/edit_task.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    
    if request.method == 'POST':
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully.'}, status=200)

    return JsonResponse({'error': 'Invalid request.'}, status=400)

def mark_task_completed(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    
    if request.method == 'POST':
        task.completed = not task.completed
        task.save()
        return JsonResponse({'message': 'Task marked as completed successfully.', 
                             "complete": task.completed,}, status=200)

    return JsonResponse({'error': 'Invalid request.'}, status=400)