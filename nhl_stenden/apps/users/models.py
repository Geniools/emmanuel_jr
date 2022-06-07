from django.db import models


class User(models.Model):
	user_id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=50)
	email = models.EmailField()
	password = models.CharField(max_length=255)
	birth_date = models.DateField()
	
	def __str__(self):
		return self.username


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
