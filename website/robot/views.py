from django.shortcuts import render
from django.db.models import Q
from .models import Room

def robot(request):
    room = Room.objects.all()
    if request.method =='POST':
        search = request.POST.get('search')
        print(search,'==============')






    return render(request, 'robot.html')
