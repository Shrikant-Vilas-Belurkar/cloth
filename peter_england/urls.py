from django.contrib import admin
from django.urls import path
from peter_england import views

urlpatterns = [
    path('peter/',views.peter),
]
