from django.urls import path
from .views import *

urlpatterns = [
    path("", shop, name="shop"),
    path("cart", cart, name="cart"),
    path("checkout", checkout, name="checkout"),
    path("update_item", update_item, name="update_item"),
    path('update_quantity/<int:order_item_id>/<int:new_quantity>/', update_quantity, name='update_quantity'),
    path('remove_item/<int:order_item_id>/', remove_item, name='remove_item'),
    path('payout/<str:name>/<str:email>/<str:city>/<str:phone>/', sending_noti, name='sending_noti'),

    path("<slug:slug>", single_product, name="single_product"),
]