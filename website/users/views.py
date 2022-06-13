from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
from users.models import TimeSlot, User
import time

from datetime import datetime, date, time


def index(request):
    return HttpResponse("Hello, world. You're at the main index USER PAGE.")

#delete all the data in the TimeSlot table
def delete_timeslot_table(request):
    TimeSlot.objects.all().delete()
    return HttpResponse("success")

#add a row to the user table
def create_user_table(request):
    User.objects.create(user_id=232212316, username="ricka", email="yuanruike2002@outlook.com", password="Keke1234", birth_date="2012-05-06")
    return HttpResponse("success")

#add a row to the TimeSlot table
def create_timeslot_table(request):
    TimeSlot.objects.create(time_slot_id=38, start_time='10:00', end_time='10:30', date="2022-06-14", user_id_id=100001)
    return HttpResponse("success")

#!Start function of the entire page
def datepicker(request):
    daGet = date.today(); #pass the date of today to the variable
    formatted_date = daGet.strftime("%Y-%m-%d")#change the date format from 0000/00/00 to 0000-00-00
    #data_list = TimeSlot.objects.filter(date=formatted_date)
    return render(request, 'users/datepickerResult.html', {'formatted_date': formatted_date})

def datepickerResult(request):
    if request.method == "GET":
        daGet = request.GET['date']# get the date selected from the datepicker form via a get request
        da = datetime.strptime(daGet, "%m/%d/%Y") #converting the date format(string to object)
        formatted_date = da.strftime("%Y-%m-%d") #save in the variable(object to string)
        #separate each part of a date string(year-month-date)
        # y, m, d = formatted_date.split('-')
        # y = int(y)
        # m = int(m)
        # d = int(d)
        #, 'y': y, 'm': m, 'd': d
        data_list = TimeSlot.objects.filter(date=formatted_date)#retrive the rows(booking info)of a specific date from database for the further validation
        data_listCount = TimeSlot.objects.filter(date=formatted_date).count()#count how many rows of info are in that date(useless,just for future use)
        #timeslots object is defined below (from 5pm to 8pm)
        timeslots = [{"startTime": '17:00', "endTime": '17:30', "period": '17:00 – 17:30'},
                     {"startTime": '17:30', "endTime": '18:00', "period": '17:30 – 18:00'},
                     {"startTime": '18:00', "endTime": '18:30', "period": '18:00 – 18:30'},
                     {"startTime": '18:30', "endTime": '19:00', "period": '18:30 – 19:00'},
                     {"startTime": '19:00', "endTime": '19:30', "period": '19:00 – 19:30'},
                     {"startTime": '19:30', "endTime": '20:00', "period": '19:30 – 20:00'},
                     ]
        if datetime.date(da) < datetime.now().date():
            return HttpResponse("Date should be upcoming (tomorrow or later)")
        elif datetime.date(da).isoweekday() in (7, 6):
            return HttpResponse("Date should not be in weekends (sat or sun)")
        else:#send the objects/values to the frontend
            return render(request, 'users/datepickerResult.html',
                          {'timeslots': timeslots, 'data_listCount': data_listCount, 'data_list': data_list,
                           'formatted_date': formatted_date})#data_listCount is useless,it if for future use


# code for converting 12hour time to 24hour time format
# def standard_to_military_time(s):
#     h, m = s.split(':')
#     h = int(h)
#     m, noon = m.split(' ')
#     if noon == 'p.m.' and h != 12:
#         h += 12
#     return '{:02d}:{}'.format(h, m)

# code for validating(after receive the post request)
def validate(request):
    if request.method == 'POST':
        datePosted = request.POST["date"]  # get date passed from the post-form
        theStartTime = request.POST['start_time']  # get theStartTime of a slot from the post request
        theEndTime = request.POST['end_time']  # get theEndTime of a slot from the post request
        userId = request.POST["userId"]  # get the userId of the user logged in from the post request
        userCheckId = TimeSlot.objects.filter(date=datePosted,
                                              start_time=theStartTime).first()  # count the total rows in the timeslot table
        countUser = TimeSlot.objects.filter(user_id_id=userId).count()  # count how many slots the user has booked
        rowscalculate = TimeSlot.objects.count()  # count the total rows in the timeslot table
        time_slot_id = rowscalculate + 1  # the row number default of the new row to be added to the database
        if userCheckId == None:  # if the certain timeslot has not been booked/else:the time slot is booked by others
            if countUser < 2:  # if the user has booked less than two timeslot/else:error
                TimeSlot.objects.create(time_slot_id=time_slot_id, start_time=theStartTime, end_time=theEndTime,
                                        date=datePosted, user_id_id=userId)#insert a new line of booking information into the timeSlot table
                # dict is the success booked info to be showed in the validate.html
                dict = {
                    'datePosted': datePosted,
                    'theStartTime': theStartTime,
                    'theEndTime': theEndTime,
                    'userId': userId,
                }
                return render(request, 'users/validate.html', dict)
            else:
                return HttpResponse("cannot book more than two timeslots")
        else:
            return HttpResponse("been booked by others")
