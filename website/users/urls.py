import contact as contact
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from . import views

urlpatters = [
	path('admin/',admin.site.urls),
	path('',views.Insertrecord)
]

urlpatterns = [
	path('', index, name='index_user'),
]
