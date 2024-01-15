from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("return-policy", return_policy, name="return_policy"),
]