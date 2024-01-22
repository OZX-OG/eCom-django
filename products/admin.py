from django.contrib import admin
from .models import *

admin.site.site_title = "OZX-OG"
admin.site.site_header = "OZX-OG"


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'device','name', 'email']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'categories', 'price', 'anchor_price','date','is_active']
    list_editable = ['price','categories' , 'anchor_price', 'is_active']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'date_order', 'complete']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'order','quantity',  "date_added"]

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'order','name', 'email', 'city', 'phone_number']

class OfferAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'percentage', 'finish_date']
    list_editable = ['product', 'percentage', 'finish_date']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Categories)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
admin.site.register(Offer, OfferAdmin)