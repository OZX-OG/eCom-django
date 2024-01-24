from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    device = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        if self.name:
            return str(self.user)
        else:
            return str(self.device)

class Categories(models.Model):
    categories = models.CharField(max_length=25)
    
    def __str__(self):
        return self.categories

class Product(models.Model):
    name = models.CharField(max_length = 100)
    discription = models.TextField()

    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
 
    price = models.FloatField()
    anchor_price = models.FloatField()

    product_image = models.ImageField(upload_to = "product", null=True)

    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    slug = AutoSlugField(unique=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitem = self.orderitem_set.all()
        total = sum( [ item.get_total for item in orderitem ] )
        return total

    @property
    def get_cart_item(self):
        orderitem = self.orderitem_set.all()
        total = sum( [ item.quantity for item in orderitem ] )
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product)
    
    @property
    def get_total(self):
        return self.product.price * self.quantity
    

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True)
    phone_number = PhoneNumberField()
    date = models.DateTimeField(auto_now_add=True, null=True)
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Processed", "Processed"),
        ("Closed", "Closed"),
    )
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default="Pending", null=True)


    def __str__(self):
        return self.name

class Offer(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True)
    percentage = models.IntegerField()
    finish_date = models.DateField()

    def __str__(self):
        return str(self.product)
