from django.contrib import admin
from django.urls import path, include
from .views import robot

urlpatterns = [
    path('', robot, name='robot'),
]
