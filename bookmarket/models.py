from django.db import models

# Create your models here.
class Product(models.Model):
    p_id = models.IntegerField (default = 0)
    title = models.CharField(max_length = 40)
    category = models.CharField(max_length = 40)
    author = models.CharField(max_length = 40)
    subject =models.CharField(max_length = 40)
    state =models.CharField(max_length = 5)
    def __str__(self):
        return self.title +"/"+ self.state

class Candidate(models.Model):
    c_id = models.IntegerField(default =0)
    c_name = models.CharField(max_length = 40)
    c_hp = models.IntegerField(default=0)
    def __str__(self):
        return self.c_name

class Sel_Reg (models.Model):
    p_id = models.ForeignKey(Product)
    s_id = models.IntegerField()
    s_name = models.CharField(max_length = 40)
    s_hp =models.CharField(max_length = 40)
    register_date =models.DateTimeField()
    init_price =models.IntegerField()
    imm_price =models.IntegerField()
    closing_date=models.DateTimeField()
    def __str__(self):
        return self.s_name

class Bid(models.Model):
    p_id = models.ForeignKey(Product)
    c_id = models.IntegerField()
    bid_date= models.DateTimeField()
    bid_price=models.IntegerField()
    priority =models.IntegerField()
