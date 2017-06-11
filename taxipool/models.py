from __future__ import unicode_literals
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User
from django.db import models

import datetime
import os


class Seek_Taxi(models.Model):

    SEEKING = 'SE1'
    SFAIL = 'SF1'
    SSUCC = 'SS1'
    SCANC = 'SC1'
    CTCHOICE = (
        (SEEKING, 'Seeking'),
        (SFAIL, 'Sefail'),
        (SSUCC, 'Sesucc'),
        (SCANC, 'Secanc'),
    )
    departure = models.CharField(max_length = 40)
    destination = models.CharField(max_length = 40)
    depart_date = models.DateField()
    depart_time = models.TimeField()
    num_person = models.IntegerField(max_length = 4)
    now_person = models.IntegerField(default = 1)
    content = models.CharField(max_length = 100)
    condition = models.CharField(max_length = 10, choices = CTCHOICE,default = SEEKING)
    seeker = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.departure + " / " + self.destination

class Attend_Passenger(models.Model):
    attend_date = models.DateTimeField()
    comment = models.CharField(max_length = 100)

    taxi = models.ForeignKey(Seek_Taxi, on_delete=models.CASCADE)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
