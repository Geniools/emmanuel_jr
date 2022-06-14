from django.db import models

<<<<<<< HEAD
=======
# Create your models here.
from django.db import models

# Create your models here.

>>>>>>> c1b84b1f0289d420431792bef48d04548f3b0e8f

class Zone(models.Model):
    zone_id = models.AutoField(primary_key=True)
    zone_data = models.CharField(max_length=255)

<<<<<<< HEAD
=======

>>>>>>> c1b84b1f0289d420431792bef48d04548f3b0e8f
    def __str__(self):
        return self.zone_id


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    zone_id = models.ForeignKey(Zone, on_delete=models.CASCADE)

    def __str__(self):
<<<<<<< HEAD
        return self.room_id
=======
        return self.room_id
>>>>>>> c1b84b1f0289d420431792bef48d04548f3b0e8f
