from django.contrib import admin
<<<<<<< HEAD
from django.urls import path
from .import views


urlpatterns = [
    path("robot", views.room_display)
]
#name='room_display'
=======
from django.urls import path, include
from .views import robot

urlpatterns = [
    path('', robot, name='robot'),
]
>>>>>>> e53156026e99992fc2c9f313e19bf568677da220
