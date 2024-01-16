from django.contrib import admin
from .models import *

admin.site.site_title = "OZX-OG"
admin.site.site_header = "OZX-OG"


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'categories', 'price', 'anchor_price','date','is_active']
    list_editable = ['price','categories' , 'anchor_price', 'is_active']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_order', 'complete']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'order','quantity',  "date_added"]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Categories)
admin.site.register(product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)