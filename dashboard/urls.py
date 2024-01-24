from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="dash_index"),
    path("Order_Details/<int:pk>", order_details, name="order_details"),
    path("all_order", all_order, name="all_order"),
    path("signin", signin, name="signin"),
    path('logout/', logoutUser, name='logout'),

    path("todoList", todolist, name="dash_todolist"),
    path('add_task/', add_task, name='add_task'),
    path('edit_task/<int:task_id>/', edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('mark_task_completed/<int:task_id>/', mark_task_completed, name='mark_task_completed'),
]