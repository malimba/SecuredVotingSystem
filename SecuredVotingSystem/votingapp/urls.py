from django.urls import path
from .views import Home, OTP, vote
app_name = 'votingapp'

urlpatterns = [
    path('', Home, name='Home'),
    path('otp', OTP, name='otp'),
    path('vote', vote, name='vote'),
]