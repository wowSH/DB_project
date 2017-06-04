from __future__ import unicode_literals

from django.db import models

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

    recruiter = models.ForeignKey(Recruiter, on_delete = models.CASCADE)
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
