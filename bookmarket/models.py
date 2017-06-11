from __future__ import unicode_literals
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User
from django.db import models

import datetime
import os
# Create your models here.


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


class Product_Register(models.Model):
    title = models.CharField(max_length = 40)
    SELLING = 'SE'
    SFAIL = 'SF'
    SSUCC = 'SS'
    SCANC = 'SC'
    CTCHOICE = (
        (SELLING, 'Selling'),
        (SFAIL, 'Sfail'),
        (SSUCC, 'Ssucc'),
        (SCANC, 'Scanc'),
    )
    category = models.CharField(max_length = 40)
    author = models.CharField(max_length = 40, null=True)
    subject = models.CharField(max_length = 40)
    state = models.CharField(max_length = 5)
    condition = models.CharField(max_length = 10, choices = CTCHOICE,default = SELLING)
    register_date = models.DateTimeField()

    current_price = models.IntegerField(default = 0)
    imm_price = models.IntegerField()
    init_price = models.IntegerField(max_length = imm_price)
    closing_date = models.DateTimeField()

    image = ProcessedImageField(
        upload_to=user_directory_path,
        processors=[ResizeToFill(160, 160)],
        format='JPEG',
        options={'quality': 60}
    )
    
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title +"/"+ self.state

class Bid_Candidate(models.Model):
    bid_date = models.DateTimeField()
    bid_price = models.IntegerField()

    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product_Register, on_delete=models.CASCADE)