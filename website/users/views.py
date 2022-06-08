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
    TimeSlot.objects.create(time_slot_id=14, start_time='09:30', end_time='10:30', date="2022-02-02", user_id_id=100001)
    TimeSlot.objects.create(time_slot_id=15, start_time='10:30', end_time='11:30', date="2022-02-02", user_id_id=100001)
    TimeSlot.objects.create(time_slot_id=16, start_time='11:30', end_time='12:30', date="2022-02-02", user_id_id=100001)
    TimeSlot.objects.create(time_slot_id=17, start_time='12:30', end_time='13:30', date="2022-02-02", user_id_id=100001)
    TimeSlot.objects.create(time_slot_id=18, start_time='13:30', end_time='14:30', date="2022-02-02", user_id_id=100001)
    TimeSlot.objects.create(time_slot_id=19, start_time='14:30', end_time='15:30', date="2022-02-02", user_id_id=100001)
    TimeSlot.objects.create(time_slot_id=20, start_time='15:30', end_time='16:30', date="2022-02-02", user_id_id=100001)
    TimeSlot.objects.create(time_slot_id=21, start_time='16:30', end_time='17:30', date="2022-02-02", user_id_id=100001)
    return HttpResponse("success")


def datepicker(request):
    formatted_date = "2022-01-01"
    data_list = TimeSlot.objects.filter(date=formatted_date)
    return render(request, 'users/datepickerResult.html', {'data_list': data_list, 'formatted_date': formatted_date})
    # return render(request, 'users/datepicker.html')


def datepickerResult(request):
    if request.method == "GET":
        daGet = request.GET['date']
        da = datetime.strptime(daGet, "%m/%d/%Y")
        formatted_date = da.strftime("%Y-%m-%d")
        data_list = TimeSlot.objects.filter(date=formatted_date)
        return render(request, 'users/datepickerResult.html',
                      {'data_list': data_list, 'formatted_date': formatted_date, 'da': da})


def standard_to_military_time(s):
    h, m = s.split(':')
    h = int(h)
    m, noon = m.split(' ')
    if noon == 'p.m.' and h != 12:
        h += 12
    return '{:02d}:{}'.format(h, m)


def validate(request):
    if request.method == 'POST':
        # var = request.POST.get("dateinfo1", "dateinfo2")
        datePosted = request.POST["date"]
        print(datePosted)
        # dateFormatted = datetime.strptime(datePosted , "%d %B, %Y")
        # # print(da)
        # date = dateFormatted.strftime("%Y-%m-%d")
        # start_time= request.POST["start_time"]
        theTime = request.POST['start_time']
        formatted_time = standard_to_military_time(theTime)
        userId = request.POST["userId"]
        # daTime = request.POST["date"] +' '+ request.POST['start_time'].rstrip(" a.m.").rstrip(" p.m.")
        # dti = datetime.strptime(daTime, "%Y-%m-%d %H:%M")
        # formatted_time = dti.strftime("%H:%M")
        userCheckId = TimeSlot.objects.filter(date=datePosted, start_time=formatted_time).first().user_id_id
        print(formatted_time)
        if userCheckId == 100001:
            TimeSlot.objects.filter(date=datePosted, start_time=formatted_time).update(user_id_id=userId)
            dict = {
                'var1': datePosted,
                'var2': formatted_time,
                'var3': userId,
                # 'urlp': urlp
            }
            return render(request, 'users/validate.html', dict)
        else:
            return HttpResponse("been booked by others")
