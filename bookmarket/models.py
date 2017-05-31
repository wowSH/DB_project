from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Seller (models.Model):
    name = models.CharField(max_length = 40)
    hp = models.CharField(max_length = 40)

    def __str__(self):
        return self.s_name

class Product_Register(models.Model):
    title = models.CharField(max_length = 40)
    category = models.CharField(max_length = 40)
    author = models.CharField(max_length = 40)
    subject = models.CharField(max_length = 40)
    state = models.CharField(max_length = 5)
    condition = models.CharField(max_length = 5)
    
    register_date = models.DateTimeField()
    init_price = models.IntegerField()
    imm_price = models.IntegerField()
    closing_date = models.DateTimeField()
    
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title +"/"+ self.state

class Candidate(models.Model):
    name = models.CharField(max_length = 40)
    hp = models.IntegerField(default=0)
   
    bidding = models.ManyToManyField(Product_Register, through='Bid')
    
    def __str__(self):
        return self.c_name


class Bid(models.Model):
    bid_date = models.DateTimeField()
    bid_price = models.IntegerField()
    priority = models.IntegerField()
   
    product = models.ForeignKey(Product_Register, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    