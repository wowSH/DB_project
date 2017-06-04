from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Seeker (models.Model):
    name = models.CharField(max_length = 40)
    hp = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class Seek_Taxi(models.Model):
    title = models.CharField(max_length = 40)
#    DELIVERY = 'DE'
#    ELECTRONIC = 'EL'
#    ETC = 'ET'
#    CTCHOICE = (
#        (DELIVERY, 'Delivery'),
#        (COSMETIC, 'Cosmetic'),
#        (ELECTRONIC, 'Electronic'),
#        (ETC, 'Etc'),
#    )
#    category = models.CharField(max_length = 40, choices = CTCHOICE,default = ETC)

    departure = models.CharField(max_length = 40)
    destination = models.CharField(max_length = 40)
    depart_date = models.DateField()
    depart_time = models.TimeField()
    num_person = models.IntegerField()
    content = models.CharField(max_length = 100)

    seeker = models.ForeignKey(Seeker, on_delete = models.CASCADE)
    def __str__(self):
        return self.departure + " / " + self.destination

class Passenger(models.Model):
    name = models.CharField(max_length = 40)
    hp = models.IntegerField(default=0)

    attending = models.ManyToManyField(Seek_Taxi, through='Attend')

    def __str__(self):
        return self.name


class Attend(models.Model):
    attend_date = models.DateTimeField()
    comment = models.CharField(max_length = 100)

    seek = models.ForeignKey(Seek_Taxi, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
