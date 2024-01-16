from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return str(self.user)


class Categories(models.Model):
    categories = models.CharField(max_length=25)
    
    def __str__(self):
        return self.categories

class product(models.Model):
    name = models.CharField(max_length = 100)
    discription = models.TextField()

    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
 
    price = models.FloatField()
    anchor_price = models.FloatField()

    produc_image = models.ImageField(upload_to = "product", null=True)

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
    product = models.ForeignKey(product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product)
    

    @property
    def get_total(self):
        return self.product.price * self.quantity