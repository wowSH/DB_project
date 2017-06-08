from django.forms import ModelForm
from .models import Party_Open

class RegisterForm(ModelForm):
    class Meta:
        model = Party_Open
        fields = ['category', 'content', 'open_date', 'closing_date', 'num_person', 'image','condition']
