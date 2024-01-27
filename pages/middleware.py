from django.urls import reverse
from django.shortcuts import redirect, render
from django.http import Http404

from django.http import HttpResponseNotFound
from django.template.loader import get_template


class RestrictAdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.path.startswith(reverse('admin:index')):
            if not request.user.is_staff:
                return redirect('error_404')
            
        if "/dashboard/" in request.path:
            if request.user.is_staff:
                if "/dashboard/signin" in request.path: 
                    return redirect('dash_index')
                
                return response
            
            else: 
                if "/dashboard/signin" in request.path: 
                    return response 
                
                return redirect('error_404')
                
                
        # print(response)
        # if response.status_code == 404 or response.status_code == 500:
        #     return redirect('error_404')

        return response