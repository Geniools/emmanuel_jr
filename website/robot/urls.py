from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path("robot", views.room_display)
]
#name='room_display'