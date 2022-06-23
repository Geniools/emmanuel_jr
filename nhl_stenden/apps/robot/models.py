from django.db import models

class Zone(models.Model):
    zone_id = models.AutoField(primary_key=True)
    zone_data = models.CharField(max_length=255)

    def __str__(self):
        return self.zone_id


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    zone_id = models.ForeignKey(Zone, on_delete=models.CASCADE)

    def __str__(self):
        return self.room_id
