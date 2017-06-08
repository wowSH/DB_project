from django.contrib import admin
from .models import Seller,Product_Register,Candidate,Bid
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Bid)
admin.site.register(Product_Register)
admin.site.register(Seller)
