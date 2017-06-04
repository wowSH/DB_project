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
class Recruiter (models.Model):
    name = models.CharField(max_length = 40)
    hp = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class Party_Open(models.Model):
    title = models.CharField(max_length = 40)
    DELIVERY = 'DE'
    COSMETIC = 'CO'
    ELECTRONIC = 'EL'
    ETC = 'ET'
    CTCHOICE = (
        (DELIVERY, 'Delivery'),
        (COSMETIC, 'Cosmetic'),
        (ELECTRONIC, 'Electronic'),
        (ETC, 'Etc'),
    )
    category = models.CharField(max_length = 40, choices = CTCHOICE,default = ETC)
    content = models.CharField(max_length = 40)

    open_date = models.DateTimeField()
    num_person = models.IntegerField()
    closing_date = models.DateTimeField()
    image = models.ImageField(upload_to=user_directory_path, default =0)

    recruiter = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.title

class Applicant(models.Model):
    name = models.CharField(max_length = 40)
    hp = models.IntegerField(default=0)

    applying = models.ManyToManyField(Party_Open, through='Apply')

    def __str__(self):
        return self.name


class Apply(models.Model):
    apply_date = models.DateTimeField()
    comment = models.CharField(max_length = 100)

    party = models.ForeignKey(Party_Open, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
