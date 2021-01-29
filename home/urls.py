from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
    path('', home, name="home"),
    path('my_logout/', my_logout, name="logout"),

]
