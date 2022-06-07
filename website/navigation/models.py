from django.db import models


# Create your models here.
class Navigation(models.Model):
    floor_nr = models.IntegerField()
