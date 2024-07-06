from django.contrib import admin
from django.urls import path
from blackberry import views

urlpatterns = [
    path('blackberry/',views.black),
]
