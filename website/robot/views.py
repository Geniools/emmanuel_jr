from django.shortcuts import render
from django.http import HttpResponse


def robot(request):
    return render(request, 'robot.html')
