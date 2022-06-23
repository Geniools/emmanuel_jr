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

class Zone(models.Model):
  zone_id = models.AutoField(primary_key=True)
  zone_data = models.CharField(max_length=255)

  def __str__(self):
    return self.zone_id

class Feedback(models.Model):
  feedback_id = models.AutoField(primary_key=True)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  topic = models.CharField(max_length=50)
  content = models.TextField()
  date = models.DateField()

  def __str__(self):
    return self.topic

class TimeSlot(models.Model):
	time_slot_id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	start_time = models.TimeField()
	end_time = models.TimeField()
	date = models.DateField()
	
	def __str__(self):
		return self.start_time + " - " + self.end_time + ": " + self.date