from django.contrib import admin
from .models import Apply_Applicant,Party_Open

#reload(sys)
#sys.setdefaultencoding('utf-8')
# Register your models here.
admin.site.register(Apply_Applicant)
admin.site.register(Party_Open)
