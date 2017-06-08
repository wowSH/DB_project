from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import RegisterForm

from django.db import connection, transaction

import datetime

# Create your views here.
from django.utils import timezone
import datetime

# Create your views here.
def index(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM bookmarket_product_register")
                    
    rows = dictfetchall(cursor)
    context = {"rows": rows}
    return render(request, 'bookmarket/index.html', context)
    
    #return render(request, 'bookmarket/index.html')
    

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
        )
        new_product.image = request.FILES['image']
        new_product.seller = request.user
        new_product.register_date = datetime.datetime.now()
        new_product.save()
        return redirect('bookmarket:index')
    else:
        form = RegisterForm()
    return render(request, 'bookmarket/index.html', {'form': form})

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
        
    
def searching(request):
    cursor = connection.cursor()
    selected_category = request.POST['selected_category']
    keyword = request.POST['keyword']
    
    params = {
        'category' : '%'+selected_category+'%',
        'keyword' : '%'+keyword+'%',
    }
    
    #cursor.execute("SELECT * FROM bookmarket_product_register WHERE (category = %(category)s AND (title LIKE %%(keyword)s% OR author LIKE %%(keyword)s% OR subject LIKE %%(keyword)s%))",
    cursor.execute("SELECT * FROM bookmarket_product_register")
                    
    rows = dictfetchall(cursor)
    context = {"rows": rows}
    return render(request, 'bookmarket/index.html', context)
    
