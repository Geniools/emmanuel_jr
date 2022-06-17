from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from users.models import TimeSlot, User
from datetime import datetime

# alter table tbname auto_increment=1;

def index(request):
    return HttpResponse("Hello, world. You're at the main index USER PAGE.")

# delete all the data in the TimeSlot table
def delete_timeslot_table(request):
    TimeSlot.objects.all().delete()
    return HttpResponse("success")

# add a row to the user table
def create_user_table(request):
    User.objects.create(user_id=232212316, username="ricka", email="yuanruike2002@outlook.com", password="Keke1234",
                        birth_date="2012-05-06")
    return HttpResponse("success")

# add a row to the TimeSlot table
def create_timeslot_table(request):
    TimeSlot.objects.create(time_slot_id=38, start_time='10:00', end_time='10:30', date="2022-06-14", user_id_id=100001)
    return HttpResponse("success")

#booking_info_submit_form define
class Submitdatepickerform(forms.Form):
    date_selected = forms.DateField(widget=forms.HiddenInput(),initial="value")
    start_time_of_slot = forms.TimeField(widget=forms.HiddenInput(),initial="value")
    end_time_of_slot = forms.TimeField(widget=forms.HiddenInput(),initial="value")


#datepicker_form define
class Selectdateform(forms.ModelForm):
    class Meta:
        model = TimeSlot
        exclude = ('end_time', 'start_time', 'user_id', 'time_slot_id')

def datepicker_result(request):
    if request.method == 'POST':
        form = Submitdatepickerform(request.POST)
        if form.is_valid():
            date_posted = form.cleaned_data['date_selected']
            # get date passed from the post-form
            the_start_time = form.cleaned_data['start_time_of_slot']
            # get the_start_time of a slot from the post request
            the_end_time = form.cleaned_data['end_time_of_slot']
            # get the userid from session
            request.session['member_id'] = "232212314"
            user_id =  request.session['member_id']  # get the user_id from the session
            # convert the object time to string time for validating purpose
            formatted_start_time = the_start_time.strftime('%H:%M')
            formatted_end_time = the_end_time.strftime('%H:%M')
            # pass the parameters to the function to check if the time is within the defined range
            if timedata_validation(formatted_start_time, formatted_end_time):
                if date_posted < datetime.now().date():
                    return HttpResponse("Date should be upcoming (tomorrow or later)")
                elif date_posted.isoweekday() in (7, 6):
                    return HttpResponse("Date should not be in weekends (sat or sun)")
                else:
                    user_booked_time = TimeSlot.objects.filter(user_id_id=user_id).count()  # count how many slots the user has booked
                    # check if the slot selected is booked by others
                    check_if_value_exist = TimeSlot.objects.filter(date=date_posted, start_time=the_start_time).exists()
                    if not check_if_value_exist:
                        # check if the user has booked more than two slots
                        if user_booked_time < 2:
                            # a new row of booking info is saved in the database
                            TimeSlot.objects.create(start_time=the_start_time, end_time=the_end_time, date=date_posted, user_id_id=user_id)
                            return HttpResponse("You successfully booked this timeslot")
                        else:
                            return HttpResponse("cannot book more than two timeslots")
                    else:
                        return HttpResponse("This slot is booked by others")
            else:
                return HttpResponse("This slot is not allowed to book")
        else:
            return HttpResponse("Sql injections not allowed")
    # if section:for getting the date submitted by user and initialize the data to be shown
    if request.method == "GET":
        #if the link is with parameters, meaning it is not the first time visiting the webpage(date is selected and sent)
        if len(request.GET.keys()) != 0:
            # initialize the dateInput form and pass it to a form variable
            date_select_form = Selectdateform()
            # initialize the dateInput form and pass it to a form variable
            form = Selectdateform(request.GET)
            if form.is_valid():
                # get the date submitted and put it in a variable for further use(cleaned_data:validate the datatype of the formfield.
                formatted_date = form.cleaned_data['date']  # get the date selected from the datepicker form via a get request
                return_value = loading_validation(formatted_date)
                # output the results of checking the time selected period from the loading_validation function
                if return_value == "weekendSelected":
                    return HttpResponse("Date should not be in weekends (sat or sun)")
                elif return_value == "wrongDateSelected":
                    return HttpResponse("Date should be upcoming (tomorrow or later)")
                else:
                    # return the display and values of the form to the frontend
                    return render(request, 'users/datepickerResult.html',
                                  {'timeslots': return_value['timeslots'], 'data_listCount': return_value['data_listCount'],
                                   'data_list': return_value['data_list'],
                                   'formatted_date': formatted_date,
                                   'date_select_form': date_select_form})
            else:
                return HttpResponse("there are sql injections")
        else:
            #else section:for the first time to enter the webpage
            #initialize the dateInput form and pass it to a form variable
            date_select_form = Selectdateform()
            # set the date of today as the default date when entering the webpage
            formatted_date = datetime.now().date()
            # return a bunch of values by calling the function
            return_value = loading_validation(formatted_date)
            # return the display and values of the form to the frontend
            return render(request, 'users/datepickerResult.html',
                          {'timeslots': return_value['timeslots'], 'data_listCount': return_value['data_listCount'], 'data_list': return_value['data_list'],
                           'formatted_date': formatted_date,
                           'date_select_form': date_select_form})

def timeslot_list():
    timeslots = [{"startTime": '17:00', "endTime": '17:30', "period": '17:00 – 17:30'},
                 {"startTime": '17:30', "endTime": '18:00', "period": '17:30 – 18:00'},
                 {"startTime": '18:00', "endTime": '18:30', "period": '18:00 – 18:30'},
                 {"startTime": '18:30', "endTime": '19:00', "period": '18:30 – 19:00'},
                 {"startTime": '19:00', "endTime": '19:30', "period": '19:00 – 19:30'},
                 {"startTime": '19:30', "endTime": '20:00', "period": '19:30 – 20:00'},
                 ]
    return timeslots

def timedata_validation(validate_starttime_value, validate_endtime_value):
    # get the timeslots defined by calling the function
    timeslots = timeslot_list()
    for eachRow in timeslots:
        # check if the timeslot selected from the webpage meets the data in the timeslots(list)
        if eachRow["startTime"] == validate_starttime_value and eachRow["endTime"] == validate_endtime_value:
            # print(eachRow["startTime"])
            # print(validate_starttime_value)
            # print(validate_endtime_value)
            return True
    return False

def loading_validation(formatted_date):
    # check if the date selected is in weekend or in the past
    if formatted_date < datetime.now().date():
        return_value = "wrongDateSelected"
        return return_value
    elif formatted_date.isoweekday() in (7, 6):
        return_value = "weekendSelected"
        return return_value
    else:
        # retrieve the rows(booking info)of a specific date(useless,just for future use)
        data_list = TimeSlot.objects.filter(date=formatted_date)
        # count how many rows of info are in that date(useless,just for future use)
        data_list_count = TimeSlot.objects.filter(date=formatted_date).count()
        # get the timeslots defined by calling the function
        timeslots = timeslot_list()
        # create another column in timeslots list for saving the form info and form format
        for eachRow in timeslots:
            form = Submitdatepickerform(
                initial={'date_selected': formatted_date, 'start_time_of_slot': eachRow["startTime"],
                         'end_time_of_slot': eachRow["endTime"]})
            eachRow["form"] = form
            check_if_value_exist = TimeSlot.objects.filter(date=formatted_date, start_time=eachRow["startTime"]).exists()
            # create another column in timeslots list for showing the booking status in the webpages
            if check_if_value_exist:
                eachRow["bookingStatus"] = "Booked"
            else:
                eachRow["bookingStatus"] = "NotBooked"
        # pass all the variables to be sent to the webpage to a dictionary
        return_value = {"timeslots": timeslots,"data_listCount": data_list_count,'data_list': data_list,'formatted_date': formatted_date}
        return return_value


