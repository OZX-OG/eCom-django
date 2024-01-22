from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="dash_index"),
    path("todoList", todolist, name="dash_todolist"),
    path("Order_Details", order_details, name="order_details"),
    path("all_order", all_order, name="all_order"),
]