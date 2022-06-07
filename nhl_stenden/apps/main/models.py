from django.db import models

class User(models.Model):
  user_id = models.AutoField(primary_key=True)
  username = models.CharField(max_length=50)
  email = models.EmailField()
  password = models.CharField(max_length=255)
  birth_date = models.IntegerField()
  
  def __str__(self):
    return self.username
