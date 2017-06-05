from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import RegisterForm

import datetime

# Create your views here.
from django.utils import timezone
import datetime
# Create your views here.
def index(request):
    return render(request, 'bookmarket/index.html')

def register_new(request):
    if request.method == "POST":

        new_product = Product_Register(
            category = request.POST['category'],
            title = request.POST['title'],
            author = request.POST['author'],
            subject = request.POST['subject'],
            init_price = request.POST['init_price'],
            imm_price = request.POST['imm_price'],
            closing_date = request.POST['closing_date'],
            state = request.POST['state'],
            image = request.POST['image'],
        )
        new_product.seller = request.user
        new_product.register_date = datetime.datetime.now()
        new_product.save()
        return redirect('bookmarket:index')
    else:
        form = RegisterForm()
    return render(request, 'bookmarket/index', {'form': form})
    
