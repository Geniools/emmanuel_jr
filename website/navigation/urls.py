from django.contrib import admin
from django.urls import path
from navigation import views


urlpatterns = [
    path("navigation", views.navigation, name='navigation'),
]
