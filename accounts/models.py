from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
#from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        primary_key = True,
    )
    
    nickname = models.CharField(max_length=30)
    hp = models.CharField(max_length=15)
    
    def __str__(self):
        return "this user's nickname is %s" %(self.nickname)