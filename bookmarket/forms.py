from django.forms import ModelForm
from .models import Product_Register

class RegisterForm(ModelForm):
    class Meta:
        model = Product_Register
        fields = ['category', 'title', 'author', 'subject', 'state', 'closing_date',
        'init_price', 'imm_price', 'image']
