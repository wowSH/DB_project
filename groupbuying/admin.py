from django.contrib import admin
from .models import Recruiter,Party_Open,Applicant,Apply
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Register your models here.
admin.site.register(Recruiter)
admin.site.register(Party_Open)
admin.site.register(Applicant)
admin.site.register(Apply)
