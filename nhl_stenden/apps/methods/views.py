import hashlib

from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.models import User

# Technical functions

def md5(string):
  return hashlib.md5(string.encode()).hexdigest()

def checkString(item, null=False, max_len=200, is_int=False):
  if not item:
    return False
  elif not null and len(str(item)) == 0:
    return False
  elif len(str(item)) > max_len:
    return False
  elif is_int and not item.isdigit():
    return False
  else:
    return True

# Request processing

def login(request):
  if checkString(request.POST.get("username"), max_len=20) and checkString(request.POST.get("password"), max_len=200):
    account = User.objects.filter(username=request.POST.get("username"), password=request.POST.get("password"))

    if account.count() > 0:
      account = account[0]
      string = str(account.username) + ":" + str(account.password) + ":" + str(account.birth_date)
      request.session['user_name'] = str(account.username)
      request.session['user_token'] = md5(string)
      return HttpResponse("true")
    else:
      return HttpResponse("false")

def registration(request):
  check_account = User.objects.filter(username=request.POST.get("username")).count()

  if checkString(request.POST.get("username"), max_len=20):
    if checkString(request.POST.get("email"), max_len=50):
      if checkString(request.POST.get("password"), max_len=200):
        if check_account == 0:
          new_user = User()
          new_user.username = request.POST.get("username")
          new_user.email = request.POST.get("email")
          new_user.password = request.POST.get("password")
          new_user.birth_date = str(round(datetime.timestamp(datetime.now())))
          new_user.save()

          string = str(new_user.username) + ":" + str(new_user.password) + ":" + str(new_user.birth_date)
          request.session['user_name'] = str(new_user.username)
          request.session['user_token'] = md5(string)
          
          return HttpResponse("true")

  return HttpResponse("false")