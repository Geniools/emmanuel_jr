from django.contrib import admin
from django.urls import path, include
from django.urls import path, include
from . import views


urlpatterns = [
    path('livestream/', views.livestream),
    path('roomSearch/', views.roomSearch),
    path('startTheRobot/', views.startTheRobot),
    path('stopTheRobot/', views.stopTheRobot),
    path('turnTheRobot/', views.turnTheRobot),
    # path('create_room_table/', views.create_room_table),
    # path('create_zone_table/', views.create_zone_table),
]
