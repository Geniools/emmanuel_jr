from django.shortcuts import render
from django.http import HttpResponse
from robot.models import Room

# Create your views here.
def robot(request):
    if request.method == 'POST':
        if 'roomnumber' in request.POST.keys():
            controlRobot = request.POST['roomnumber']
            if Room.objects.filter(room_id=request.POST['roomnumber']).exists():
                # return render(req, 'robot/liveStream.html',{'message': "directing to room"})
                success = 'directing to room' + request.POST['roomnumber'] + '...'
                return HttpResponse(success)
            else:
                # return render(req, 'robot/liveStream.html',{'message': "input does not match any data in the database"})
                success = 'input does not match any data in the database'
                return HttpResponse(success)