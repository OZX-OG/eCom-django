from django.urls import path
from .views import *

urlpatterns = [
    path("", shop, name="shop"),
    path("<slug:slug>", single_product, name="single_product"),
    path("cart", cart, name="cart"),
    path("checkout", checkout, name="checkout"),
]