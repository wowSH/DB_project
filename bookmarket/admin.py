from django.contrib import admin
from .models import Product_Register,Bid_Candidate
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Register your models here.
admin.site.register(Bid_Candidate)
admin.site.register(Product_Register)
