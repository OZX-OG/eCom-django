from django.contrib import admin
from .models import *

app_name = "OZX-OG"

admin.site.register(product)
admin.site.register(Categories)