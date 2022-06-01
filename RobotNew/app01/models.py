# Create your models here.
# class Article(models.Model):
#  """文章模型"""
#   title = models.CharField('标题', max_length=200, db_index=True)
#   pub_date = models.DateTimeField('发布时间', null=True)
from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()


# create table app01_userinfo(
#     id bigint auto_increment primary key,
#     name varchar(32),
#     password varchar(64),
#     age int
# )
class Time(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


