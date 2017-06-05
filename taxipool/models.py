from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import datetime
import os
def set_filename_format(now, instance, filename):
    """ file format setting
    e.g)
        {username}-{date}-{microsecond}{extension} hjh-2016-07-12-158859.png
    """
    return "{username}-{date}-{microsecond}{extension}".format(
        username=instance.user.username,
        date=str(now.date()),
        microsecond=now.microsecond,
        extension=os.path.splitext(filename)[1],
    )

def user_directory_path(instance, filename):
    """
    image upload directory setting
    e.g)
        images/{year}/{month}/{day}/{username}/{filename}
        images/2016/7/12/hjh/hjh-2016-07-12-158859.png
    """
    now = datetime.datetime.now()
    path = "images/{year}/{month}/{day}/{username}/{filename}".format(
        year=now.year,
        month=now.month,
        day=now.day,
        username=instance.user.username,
        filename=set_filename_format(now, instance, filename),
    )
    return path

# Create your models here.
class Seeker (models.Model):
    name = models.CharField(max_length = 40)
    hp = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class Seek_Taxi(models.Model):

    SEEKING = 'SE'
    SFAIL = 'SF'
    SSUCC = 'SS'
    SCANC = 'SC'
    CTCHOICE = (
        (SEEKING, 'Seeking'),
        (SFAIL, 'Sfail'),
        (SSUCC, 'Ssucc'),
        (SCANC, 'Scanc'),
    )
    departure = models.CharField(max_length = 40)
    destination = models.CharField(max_length = 40)
    depart_date = models.DateField()
    depart_time = models.TimeField()
    num_person = models.IntegerField()
    register_date = models.DateTimeField()
    content = models.CharField(max_length = 100)
    condition = models.CharField(max_length = 5, choices = CTCHOICE,default = SEEKING)
    seeker = models.ForeignKey(User, on_delete = models.CASCADE)
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
