from django.forms import ModelForm
from .models import Seek_Taxi

class RegisterForm(ModelForm):
    class Meta:
        model = Seek_Taxi
        fields = ['departure', 'destination', 'depart_date', 'depart_time',
        'num_person', 'content', 'condition']
