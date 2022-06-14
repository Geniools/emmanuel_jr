from urllib import request
from django.shortcuts import render, HttpResponse
# from .models import Profile
# Create your views here.
from .models import Room

def robot(request):
        if request.method == 'POST':
            if 'room' in request.POST.keys():
                if request.POST.get('room')=="":
                    invalid="You can not leave it blank"
                    return HttpResponse(invalid)
                if Room.objects.filter(room_id=request.POST.get('room')).exists():
                    redirecting = 'selected room is ' + request.POST.get('room') 
                    return HttpResponse(redirecting)
                if Room.objects.filter(room_id=request.POST.get('room')).none:
                    failed = 'there is no room that matches with the database'
                    return HttpResponse(failed)
        return render(request, 'robot.html')