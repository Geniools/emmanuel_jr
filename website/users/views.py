from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from users.models import TimeSlot, User
from datetime import datetime,timedelta
from django.contrib import messages

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
            request.session['member_id'] = "232212313"
            user_id =  request.session['member_id']  # get the user_id from the session
            # convert the object time to string time for validating purpose
            formatted_start_time = the_start_time.strftime('%H:%M')
            formatted_end_time = the_end_time.strftime('%H:%M')
            # pass the parameters to the function to check if the time is within the defined range
            if timedata_validation(formatted_start_time, formatted_end_time):
                # check if date_posted is in the past, if so the system will set today as a default and pass it to the render_values.loading_validation function to further varify
                if date_posted < datetime.now().date():
                    messages.error(request, 'Date should be upcoming (today, tomorrow or later)')
                    formatted_date = datetime.now().date()
                    return render_values(request, formatted_date)
                #check if date_posted is in weekend
                elif date_posted.isoweekday() in (7, 6):
                    messages.error(request, 'Date should not be in weekends (sat or sun)')
                    formatted_date = datetime.now().date()
                    return render_values(request, formatted_date)
                else:
                    user_booked_time = TimeSlot.objects.filter(user_id_id=user_id).count()  # count how many slots the user has booked
                    # check if the slot selected is booked by others
                    check_if_value_exist = TimeSlot.objects.filter(date=date_posted, start_time=the_start_time).exists()
                    if not check_if_value_exist:
                        # check if the user has booked more than two slots
                        if user_booked_time < 2:
                            # a new row of booking info is saved in the database
                            TimeSlot.objects.create(start_time=the_start_time, end_time=the_end_time, date=date_posted, user_id_id=user_id)
                            formatted_date = date_posted
                            messages.error(request, 'You successfully booked this timeslot')
                            return render_values(request, formatted_date)
                        else:
                            formatted_date = date_posted
                            messages.error(request, 'cannot book more than two timeslots')
                            return render_values(request, formatted_date)
                    else:
                        formatted_date = date_posted
                        messages.error(request, 'This slot is booked by others')
                        return render_values(request, formatted_date)
            else:
                formatted_date = date_posted
                messages.error(request, 'This slot is not allowed to book')
                return render_values(request, formatted_date)
        else:
            formatted_date = datetime.now().date()
            messages.error(request, 'Sql injections not allowed')
            return render_values(request, formatted_date)
    # if section:for getting the date submitted by user and initialize the data to be shown
    if request.method == "GET":
        #if the link is with parameters, meaning it is not the first time visiting the webpage(date is selected and sent)
        if len(request.GET.keys()) != 0:
            form = Selectdateform(request.GET)
            if form.is_valid():
                # get the date submitted and put it in a variable for further use(cleaned_data:validate the datatype of the formfield.
                formatted_date = form.cleaned_data['date']
                return render_values(request, formatted_date)
            else:
                formatted_date = datetime.now().date()
                messages.error(request, 'Sql injections not allowed')
                return render_values(request, formatted_date)
        else:
            #else section:for the first time to enter the webpage
            # set the date of today as the default date when entering the webpage
            formatted_date = datetime.now().date()
            return render_values(request, formatted_date)

def render_values(request,formatted_date):
    # initialize the dateInput form and pass it to a form variable
    date_select_form = Selectdateform()
    # return a bunch of values by calling the function
    return_value = loading_validation(formatted_date)
    # return the display and values of the form to the frontend
    return render(request, 'users/datepickerResult.html',
                  {'timeslots': return_value['timeslots'],
                   'formatted_date': return_value['formatted_date'],
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
            return True
    return False

def loading_validation(formatted_date):
    # check if the date selected is in weekend or in the past
    if formatted_date < datetime.now().date():
        formatted_date = datetime.now().date()
        print(formatted_date)
        return loading_validation(formatted_date)
    elif formatted_date.isoweekday() in (6,7):
        # if date selected == saturday
        if formatted_date.isoweekday() == 6 :
            # formatted_date == monday of next week
            formatted_date = datetime.today() + timedelta(days=2)
            #covert date format(object to string)
            formatted_date = formatted_date.strftime('%Y-%m-%d')
            # covert date format(string to object) and convert datetime object to date object
            formatted_date = datetime.strptime(formatted_date, '%Y-%m-%d').date()

        # if date selected == sunday
        if formatted_date.isoweekday() == 7:
            # formatted_date == monday of next week
            formatted_date = datetime.today() + timedelta(days=1)
            formatted_date = formatted_date.strftime('%Y-%m-%d')
            formatted_date = datetime.strptime(formatted_date, '%Y-%m-%d').date()
        print(formatted_date)
        return loading_validation(formatted_date)
    else:
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
        return_value = {"timeslots": timeslots,'formatted_date': formatted_date}
        return return_value

