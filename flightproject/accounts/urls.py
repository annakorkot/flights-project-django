from django.contrib import admin
from django.urls import path , include
from .views import homepage, update_profile

urlpatterns = [
    path('homepage/', homepage ,name='homepage'),
]
