# imports
from django.shortcuts import render, HttpResponse, redirect
import json
from .models import VoteNominee

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


def add_nominee(request):
    if request.method == 'POST':
        name = request.POST['name']
        photo = request.FILES['photo']
        position = request.POST['position']

        nominee = VoteNominee(name=name, photo=photo, position=position)
        nominee.save()

        return redirect('votingapp:add_nominee')  # Redirect to a success page or the desired URL

    return render(request, 'addnominee.html')
def vote(request):
    if request.method == 'GET':
        nominees = VoteNominee.objects.all()
        president = list()
        vice = list()
        for nom in nominees:
            if nom.position == 'president':
                president.append(nom)
            else:
                vice.append(nom)
        context = {'presidents':president, 'vices':vice}
        return render(request, 'vote.html', context)
    if is_ajax(request) and request.method == 'POST':

        #add votes to user
        try:
            print(request.POST)
            votes =[]
            for itm in request.POST:
                if type(itm) == str:
                    votes.append(itm.split(',')[0])
                    votes.append(itm.split(',')[1])

            successful_json = {'value':True}
            print(votes)
            #strip spaces
            for v in votes:
                votes[votes.index(v)] = v.replace(" ", "")
            for v in votes:
                print(v)
                nomObj = VoteNominee.objects.get(name=str(v))
                nomObj.votes = nomObj.votes +1
                nomObj.save()
            return HttpResponse(json.dumps(successful_json))
        except Exception as e:
            unsuccessful_json = {'value': False}
            print(e)
            return HttpResponse(json.dumps(unsuccessful_json))