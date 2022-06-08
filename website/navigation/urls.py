from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path("navigation", views.room_display,name='room_display')
]
