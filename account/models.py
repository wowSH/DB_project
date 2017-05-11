from django.db import models

# Create your models here.
class User(models.Model):
    u_id = models.IntegerField()
    name = models.CharField(max_length = 20)
    passward = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 254)
    HP = models.IntegerField ()

    def __str__(self):
        return self.name;
