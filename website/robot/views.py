from django.shortcuts import render
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
