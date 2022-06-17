from statistics import mode
from django.db import models

class User(models.Model):
  user_id = models.AutoField(primary_key=True)
  username = models.CharField(max_length=50)
  email = models.EmailField()
  password = models.CharField(max_length=255)
  birth_date = models.IntegerField()
  
  def __str__(self):
    return self.username

class Review(models.Model):
  username = models.CharField(max_length=50)
  rates = models.IntegerField()
  text = models.TextField()
  date = models.IntegerField()

  def __str__(self):
    return self.username

class Room(models.Model):
  room_id = models.IntegerField()
  zone = models.IntegerField()

  def __str__(self):
    return self.room_id
