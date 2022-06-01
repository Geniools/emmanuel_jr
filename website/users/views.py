from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
from users.models import TimeSlot, User


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
    return HttpResponse("success")

def create_timeslot_table(request):
    TimeSlot.objects.create(time_slot_id=1,  start_time='09:30', end_time='10:30', date="2022-01-01", user_id_id=100001)
    TimeSlot.objects.create(time_slot_id=2, start_time='10:30', end_time='11:30', date="2022-01-01", user_id_id=100001)
    TimeSlot.objects.create(time_slot_id=3, start_time='11:30', end_time='12:30', date="2022-01-01", user_id_id=100001)
    TimeSlot.objects.create(time_slot_id=4, start_time='12:30', end_time='13:30', date="2022-01-01", user_id_id=100001)
    return HttpResponse("success")

def datepicker(req):
    # if request.method == "GET":
    #     # data_list = Time.objects.filter(date = request.POST.get("Date"))
    #     # print(data_list)
    #     return render(req, 'datepicker.html')
    return render(req, 'users/datepicker.html')


def datepickerResult(request):
    if request.method == "GET":
        # if request.GET['time'] == '05/06/2022':
        ti = request.GET['time']
        da = datetime.strptime(ti, "%m/%d/%Y")
        # print(da)
        formatted_date = da.strftime("%Y-%m-%d")
        # print(formatted_date)
        # data_list = TimeSlot.objects.filter(date=formatted_date)
        data_list = TimeSlot.objects.all()
        #print(data_list)
        # print(formatted_date)
        return render(request, 'users/datepickerResult.html', {'data_list': data_list,'formatted_date':formatted_date,'da':da})


def livestream(req):
    return render(req, 'users/liveStream.html')
