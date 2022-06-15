from ast import Not
from urllib import request
from django.shortcuts import render, HttpResponse
# from .models import Profile
# Create your views here.
from .models import Room

def robot(request):
        if request.method == 'POST':
            if 'room' in request.POST:
                if request.POST.get('room')=="":
                    invalid="Please enter room number and you can not leave the field blank"
                    return render(request,'robot.html',{'invalid':invalid})

                elif request.POST.get('room').isnumeric()==False:
                    invalidInput="Please enter valid room number"
           
                    return render(request,'robot.html',{'invalidInput':invalidInput})
                    
                elif Room.objects.filter(room_id=request.POST.get('room')).exists():
                    redirecting = 'selected room is ' + request.POST.get('room') 
                    return render(request,'robot.html',{'redirecting':redirecting})

                elif Room.objects.filter(room_id=request.POST.get('room')).exists()==False:
                    failed = 'there is no room that matches with the database'
                    return render(request,'robot.html',{'failed':failed})
                    
        return render(request, 'robot.html')