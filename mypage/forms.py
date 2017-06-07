from django.forms import ModelForm
from .models import  Product_nickname_HP

class Nickname_HP_Form(ModelForm):
    class Meta:
        model = Product_nickname_HP
        fields = ['nickname', 'HP']