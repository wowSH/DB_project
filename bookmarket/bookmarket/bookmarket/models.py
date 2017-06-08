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
    #return "{username}-{date}-{microsecond}{extension}".format( 
    return "{username}-{date}-{microsecond}{extension}".format( 
        username=instance.seller.username, 
        p_id = str(instance.id),
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

    
    now = datetime.datetime.now() 
    path = "images/{year}/{month}/{day}/{username}/{filename}".format( 
        year=now.year, 
        month=now.month, 
        day=now.day, 
        username=instance.seller.username, 
        filename=set_filename_format(now, instance, filename), 
    )
    """
    now = datetime.datetime.now() 
    path = "images/bookmarket/{filename}".format( 
        year=now.year, 
        month=now.month, 
        day=now.day, 
        filename=set_filename_format(now, instance, filename), 
    )
    return path
    

class Product_Register(models.Model):
    title = models.CharField(max_length = 40)
    MAJOR_E = 'ME'
    MAJOR_NE = 'MN'
    LIBERAL = 'LI'
    ETC = 'ET'
    CTCHOICE = (
        (MAJOR_E, 'Major_e'),
        (MAJOR_NE, 'Major_ne'),
        (LIBERAL, 'Liberal'),
        (ETC, 'Etc'),
    )
    category = models.CharField(max_length = 40, choices = CTCHOICE, default = ETC)
    author = models.CharField(max_length = 40, null=True)
    subject = models.CharField(max_length = 40)
    state = models.CharField(max_length = 5)
    condition = models.CharField(max_length = 5)
    register_date = models.DateTimeField()
    init_price = models.IntegerField()
    imm_price = models.IntegerField()
    current_price = models.IntegerField(default = 0)
    closing_date = models.DateTimeField()

    #image = models.ImageField(upload_to=user_directory_path, default =0)
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

