from __future__ import unicode_literals
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User
from django.db import models
import datetime
import os



#http://hjh5488.tistory.com/12
def set_filename_format(now, instance, filename):
    """ file format setting
    e.g)
        {username}-{date}-{microsecond}{extension} hjh-2016-07-12-158859.png
    """
    return "{date}-{microsecond}{extension}".format(
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
    path = "images/bookmarket/{filename}".format(
        filename=set_filename_format(now, instance, filename),
    )
    return path


class Party_Open(models.Model):
    #    category = models.CharField(max_length = 40, choices = CTCHOICE,default = ETC)
    RECRUITING = 'RE'
    SFAIL = 'SF'
    SSUCC = 'SS'
    SCANC = 'SC'
    CTCHOICE = (
        (RECRUITING, 'Recruiting'),
        (SFAIL, 'Sfail'),
        (SSUCC, 'Ssucc'),
        (SCANC, 'Scanc'),
    )
    title = models.CharField(max_length = 40)

    category = models.CharField(max_length = 40)
    content = models.CharField(max_length = 40)

    open_date = models.DateTimeField()
    num_person = models.IntegerField()
    now_person = models.IntegerField(default = 1)
    closing_date = models.DateTimeField()
    image = models.ImageField(upload_to=user_directory_path, default =0)
    condition = models.CharField(max_length =10, choices = CTCHOICE,default = RECRUITING)
    recruiter = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.title

class Apply_Applicant(models.Model):
    apply_date = models.DateTimeField()
    comment = models.CharField(max_length = 100)

    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    party = models.ForeignKey(Party_Open, on_delete=models.CASCADE)
