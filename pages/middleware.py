from django.urls import reverse
from django.shortcuts import redirect, render
from django.http import Http404

from django.http import HttpResponseNotFound
from django.template.loader import get_template


class RestrictAdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(reverse('admin:index')):
            if not request.user.is_staff:
                return redirect('error_404')
                
        response = self.get_response(request)
        print(response)
        if response.status_code == 404 or response.status_code == 500:
            return redirect('error_404')

        return response