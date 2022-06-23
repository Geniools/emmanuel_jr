from django.shortcuts import render, HttpResponse
from robot.models import Room

def livestream(req):
    return render(req, 'robot/liveStream.html')

def roomSearch(req):
    if req.method == 'POST':
        if 'roomnumber' in req.POST.keys():
            controlRobot = req.POST['roomnumber']
            if Room.objects.filter(room_id=req.POST['roomnumber']).exists():
                # return render(req, 'robot/liveStream.html',{'message': "directing to room"})
                success = 'directing to room' + req.POST['roomnumber'] + '...'
                return HttpResponse(success)
            else:
                # return render(req, 'robot/liveStream.html',{'message': "input does not match any data in the database"})
                success = 'input does not match any data in the database'
                return HttpResponse(success)

def startTheRobot(req):
    if req.method == 'POST':
        if 'startRobot' in req.POST.keys() and req.POST['startRobot'] == 'startRobot':
            controlRobot = req.POST['startRobot']
            # return render(req, 'robot/liveStream.html', {'message': controlRobot})
            success = 'The request ' + controlRobot + ' sent'
            return HttpResponse(success)

def stopTheRobot(req):
    if req.method == 'POST':
        if 'stopRobot' in req.POST.keys() and 'stopRobot' in req.POST.values():
            controlRobot = req.POST["stopRobot"]
            # return render(req, 'robot/liveStream.html', {'message': controlRobot})
            success = 'The request ' + controlRobot + ' sent'
            return HttpResponse(success)

def turnTheRobot(req):
    if req.method == 'POST':
        if 'turnRobot' in req.POST.keys() and req.POST['turnRobot'] == 'turnRobot':
            controlRobot = req.POST['turnRobot']
            # return render(req, 'robot/liveStream.html', {'message': controlRobot})
            success = 'The request ' + controlRobot + ' sent'
            return HttpResponse(success)
