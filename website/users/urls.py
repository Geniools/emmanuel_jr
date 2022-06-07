from django.contrib import admin
from django.urls import path, include

from . import views
from .views import index


urlpatterns = [
	path('', index, name='index_user'),
	path('feedback/', views.feedback),
	path('rating/', views.rating),
]
