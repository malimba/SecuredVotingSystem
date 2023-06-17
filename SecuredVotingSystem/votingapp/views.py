# imports
from django.shortcuts import render, HttpResponse, redirect
import json


# Create your views here.
# view to handle ajax request
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def Home(request):
    return render(request, 'index.html')


def OTP(request):
    if request.method == 'GET':
        return render(request, 'otp.html')

    if is_ajax(request) and request.method == 'POST':
        print(request.POST)
        successful_json = {'value': True}
        unsuccessful_json = {'value': False}
        otp = request.POST['otp']
        # todo: work on retrieving and validating otp here
        if int(otp) == 1415:
            return HttpResponse(json.dumps(successful_json))
        else:
            return HttpResponse(json.dumps(unsuccessful_json))


def vote(request):
    return render(request, 'vote.html')