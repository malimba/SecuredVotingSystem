#imports
from django.shortcuts import render, HttpResponse, redirect
import json

# Create your views here.
#view to handle ajax request
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
def Home(request):
    return render(request, 'index.html')

def OTP(request):
    if request.method == 'GET':
        return render(request, 'otp.html')
def vote(request):
    return render(request, 'index.html')