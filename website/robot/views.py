from django.shortcuts import render
<<<<<<< HEAD
from .models import Room
from django.contrib import messages


# Create your views here.
def room_display(request):
    results = Room.objects.all()
    return render(request, 'robot.html', {"Room": results})
=======
from django.db.models import Q
from .models import Room


def robot(request):
    room = Room.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search')
        results = Room.objects.filter(Q(room_id__icontains=search))

        context = {
            'result': results
        }
        return render(request, 'robot.html', context)

    return render(request, 'robot.html')
>>>>>>> e53156026e99992fc2c9f313e19bf568677da220
