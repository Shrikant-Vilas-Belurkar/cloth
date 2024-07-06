from django.contrib import admin
from django.urls import path
from alley_sollay import views

urlpatterns = [
    path('alley/',views.alley),
]
