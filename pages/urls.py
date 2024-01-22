from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("return-policy", return_policy, name="return_policy"),
    path("404", error_404, {'exception': Exception('Page not Found')}, name="error_404"),
]