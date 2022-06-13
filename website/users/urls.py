from django.contrib import admin
from django.urls import path, include

from . import views
from .views import index

urlpatterns = [
    path('', index, name='index_user'),
    # rick's code here
    path('datepickerResult/', views.datepicker_result),
    path('create_timeslot_table/', views.create_timeslot_table),
    path('delete_timeslot_table/', views.delete_timeslot_table),
    path('create_user_table/', views.create_user_table),
    #path('validate/', views.validate)
]
