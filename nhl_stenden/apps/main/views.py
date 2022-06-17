import hashlib

from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Review

# Technical functions

def md5(string):
  return hashlib.md5(string.encode()).hexdigest()

def isLogin(request):
  name = request.session.get("user_name", "error")
  token = request.session.get("user_token", "error")

  if name == "error" or token == "error":
    return False

  account = User.objects.filter(username=name)

  if account.count() > 0:
    account = account[0]
    account_token = md5(str(account.username) + ":" + str(account.password) + ":" + str(account.birth_date))

    if token == account_token:
      return True
    else:
      return False
  else:
    return False


# Request processing

def home(request):
  if not isLogin(request):
    return HttpResponseRedirect("/login")

  return render(request, 'main/home.html')


def login(request):
  if isLogin(request):
    return HttpResponseRedirect("/")

  return render(request, 'main/login.html')


def registration(request):
  if isLogin(request):
    return HttpResponseRedirect("/")

  return render(request, 'main/registration.html')


def room(request):
  if not isLogin(request):
    return HttpResponseRedirect("/login")

  return render(request, 'main/room.html')


def schedule(request):
  if not isLogin(request):
    return HttpResponseRedirect("/login")

  return render(request, 'main/schedule.html')

def reviews(request):
  if not isLogin(request):
    return HttpResponseRedirect("/login")

  if request.POST.get("rates") and int(request.POST.get("rates")) > 0 and int(request.POST.get("rates")) <= 5:
    review = Review()
    review.username = request.POST.get("name")
    review.rates = request.POST.get("rates")
    review.text = request.POST.get("text")
    review.date = int(round(datetime.timestamp(datetime.now())))
    review.save()

  return render(request, 'main/reviews.html')

def media(request):
  if not isLogin(request):
    return HttpResponseRedirect("/login")

  return render(request, 'main/media.html')