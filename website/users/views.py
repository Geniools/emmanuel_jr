from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
from users.models import TimeSlot, User
import time
from datetime import datetime, date, time

def index(request):
    return HttpResponse("Hello, world. You're at the main index USER PAGE.")


def create_user_table(request):
    User.objects.create(user_id=100001, username="ricka", email="yuanruike2002@outlook.com", password="Keke1234",
                        birth_date="2012-05-06")
    User.objects.create(user_id=100002, username="rickb", email="keketty@163.com", password="Keke1234",
                        birth_date="2002-05-06")
    User.objects.create(user_id=100003, username="rickc", email="rake8848@sina.cn", password="Keke1234",
                        birth_date="2002-05-06")
    User.objects.create(user_id=100004, username="rickd", email="ruike.yuan@student.nhlstenden.com",
                        password="Keke1234", birth_date="2002-05-06")
    User.objects.create(user_id=22221111, username="rickd", email="ruike.yuan@student.nhlstenden.com",
                        password="Keke1234", birth_date="2002-05-06")
    return HttpResponse("success")

def create_timeslot_table(request):
    TimeSlot.objects.create(time_slot_id=6,  start_time='09:30', end_time='10:30', date="2022-01-01", user_id_id=100001)
    TimeSlot.objects.create(time_slot_id=7, start_time='10:30', end_time='11:30', date="2022-01-01", user_id_id=100001)
    TimeSlot.objects.create(time_slot_id=8, start_time='11:30', end_time='12:30', date="2022-01-01", user_id_id=100001)
    TimeSlot.objects.create(time_slot_id=9, start_time='12:30', end_time='13:30', date="2022-01-01", user_id_id=100001)
    return HttpResponse("success")

def datepicker(req):
    return render(req, 'users/datepicker.html')



def datepickerResult(request):
    if request.method == "GET":
        daGet = request.GET['date']
        da = datetime.strptime(daGet, "%m/%d/%Y")
        formatted_date = da.strftime("%Y-%m-%d")
        data_list = TimeSlot.objects.filter(date=formatted_date)
        return render(request, 'users/datepickerResult.html', {'data_list': data_list,'formatted_date':formatted_date,'da':da})





def validate(request):
   if request.method == 'POST':
          #var = request.POST.get("dateinfo1", "dateinfo2")
          datePosted = request.POST["date"]
          print(datePosted)
          # dateFormatted = datetime.strptime(datePosted , "%d %B, %Y")
          # # print(da)
          # date = dateFormatted.strftime("%Y-%m-%d")
         # start_time= request.POST["start_time"]
          userId= request.POST["userId"]
          daTime = request.POST["date"] +' '+ request.POST['start_time'].rstrip(" a.m.").rstrip(" p.m.")
          dti = datetime.strptime(daTime, "%Y-%m-%d %H:%M")
          formatted_time = dti.strftime("%H:%M")
          userCheckId = TimeSlot.objects.filter(date=datePosted, start_time=formatted_time).first().user_id_id
          print(userCheckId)
          if userCheckId == 100001:
              TimeSlot.objects.filter(date=datePosted, start_time=formatted_time).update(user_id_id=userId)
              dict = {
                 'var1': datePosted,
                 'var2': formatted_time,
                 'var3': userId,
                 #'urlp': urlp
              }
              return render(request, 'users/validate.html', dict)
          else:
              return HttpResponse("been booked by others")

