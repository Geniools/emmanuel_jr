from django.shortcuts import render
from django.http import HttpResponse

import users
from users.models import Feedback, User


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


def index(request):
    return HttpResponse("Hello, world. You're at the main index USER PAGE.")

def feedback(request):
    return render(request, 'users/feedback.html')

def create_feedback_table(request):
    Feedback.objects.create(feedback_id=10, topic=50, content="my review is the best because i did it", date="2022-06-06", user_id=505050)

def rating(request):
    if request.method == 'POST':
        var = request.POST['']
        form = feedbackForm(request.POST);
    if form.is_valid():
        user_id_id= form.cleaned_data['user_id_id']
        topic = form.cleaned_data['topic']
        content = form.cleaned_data['content']




