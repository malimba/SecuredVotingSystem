from django.urls import path
from .views import Home
app_name = 'votingapp'

urlpatterns = [
    path('', Home, name='Home')
]