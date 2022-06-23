from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('registration/', views.registration, name="registration"),
    path('room/', views.room, name="room"),
    path('schedule/', views.schedule, name="schedule"),
    path('reviews/', views.reviews, name="reviews"),
    path('media/', views.media, name="media"),
    # Vnizu hueta ot dalbaeba
    path('create_timeslot_table/', views.create_timeslot_table),
    path('delete_timeslot_table/', views.delete_timeslot_table),
    path('create_user_table/', views.create_user_table),
]