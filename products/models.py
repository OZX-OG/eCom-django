from django.db import models
from autoslug import AutoSlugField
from datetime import datetime


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

    date = models.DateTimeField(default=datetime.now)
    is_active = models.BooleanField(default=True)
    slug = AutoSlugField(unique=True)

    def __str__(self):
        return self.name