from django.contrib import admin
from .models import Seeker,Seek_Taxi,Passenger,Attend
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Register your models here.
admin.site.register(Seeker)
admin.site.register(Seek_Taxi)
admin.site.register(Passenger)
admin.site.register(Attend)
