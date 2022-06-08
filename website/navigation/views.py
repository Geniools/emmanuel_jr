from django.shortcuts import render
from .models import Room
from django.contrib import messages


# Create your views here.
def room_display(request):
    results = Room.objects.all()
    return render(request, 'navigation.html', results)
