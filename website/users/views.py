from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact


def index(request):
	if request.method=="POST":
		contact=Contact()
		name=request.POST.get('name')
		subject = request.POST.get('subject')
		contact.name=name
		contact.subject=subject
		contact.save()
		return HttpResponse("Thanks for the review")
	return render(request,'index.html')




