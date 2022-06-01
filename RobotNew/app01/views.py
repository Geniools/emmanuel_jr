from urllib import request


from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
# Create your views here.
from app01.models import Time


def index(request):
    return HttpResponse("HUANYINGSHIYONG")


def something(req):
    # request 是一个对象，封装了用户通过浏览器发送过来的所有请求相关数据

    # 1.获取请求方式 GET/POST
    print(req.method)

    # 2.在url上传递值 /something/?n1=123&n2=456
    print(req.GET)

    # 3.在请求体中传递数据
    print(req.POST)

    # return HttpResponse("返回内")
    # 4.内容字符串内容返回给请求者

    return render(req, 'something.html', {"title": "来了"})

    # 让浏览器重定向
    # return redirect("https://www.baidu.com")


# class ArticleCreateView(CreateView):
#  model = Article
#  form_class = ArticleForm
#  template_name = 'blog/article_form.html'


def datepicker(req):
    # if request.method == "GET":
    #     # data_list = Time.objects.filter(date = request.POST.get("Date"))
    #     # print(data_list)
    #     return render(req, 'datepicker.html')

    return render(req, 'datepicker.html')


def datepickerResult(request):
     if request.method == "GET":
         #if request.GET['time'] == '05/06/2022':
        ti = request.GET['time']
        da = datetime.strptime(ti, "%m/%d/%Y")
        #print(da)
        formatted_date = da.strftime("%Y-%m-%d")
        #print(formatted_date)
        #data_list = Time.objects.filter(date = "2022-05-06")
        data_list = Time.objects.filter(date=formatted_date)
        #print(formatted_date)
        return render(request, 'datepickerResult.html', {'data_list': data_list})


def dateTimePicker(req):
    return render(req, 'dateTimePicker.html')


def date(req):
    return render(req, 'date.html')

def orm(request):
    Time.objects.create(date="2022-05-06",start_time= '09:30',end_time= '10:30')
    Time.objects.create(date="2022-05-06", start_time='10:30', end_time='11:30')
    Time.objects.create(date="2022-05-06", start_time='11:30', end_time='12:30')
    Time.objects.create(date="2022-05-06", start_time='12:30', end_time='13:30')

    return HttpResponse("success")

def livestream(req):
    return render(req, 'liveStream.html')