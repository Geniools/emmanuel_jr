from django.shortcuts import render


# Create your views here.
def navigation(request):
    return render(request, 'navigation.html')
