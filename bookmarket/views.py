from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.db import connection, transaction

import datetime

# Create your views here.
from django.utils import timezone
import datetime


# Create your views here.
def index(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM bookmarket_product_register")
    row = dictfetchall(cursor)
    context = {"row": row}
    return render(request, 'bookmarket/index.html', context)


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
#        new_product.image = request.FILES['image']
        if new_product.init_price > new_product.imm_price :
            return render (request, 'bookmarket/error-price.html')
        new_product.seller = request.user
        new_product.register_date = datetime.datetime.now()
        new_product.condition = 'SELLING'
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
def Searching(request) :
        cursor = connection.cursor()
        selected_category =request.POST['selected_category']
        selected_titl = request.POST['selected_title']
        cursor.execute("SELECT * FROM bookmarket_product_register WHERE category = %s AND title LIKE %s OR author LIKE %s",[selected_category, '%'+selected_titl+'%' ,'%'+selected_titl+'%'] )
        row = dictfetchall(cursor)

        context = {"row":row, "selected_category":selected_category}
        return render(request, 'bookmarket/index.html', context)

@login_required()
def bidding(request):

    bid_date = datetime.datetime.now()
    bid_price = request.POST['bidding_price']
    product = Product_Register.objects.get(id=request.POST['product_id'])
    bids = Bid_Candidate.objects.filter(product=product)
    current_price1 = request.POST['current_price1']
    """
    if len(bids) == 0:
        priority = 1
    else:
        ordered_list = list(Bid_Candidate.objects.filter(product=product).order_by('bid_price').values_list('bid_price'))
        priority = ordered_list.index(bid_price)
    """
    #Product_Register.objects.raw("(SELECT * FROM ( SELECT RANK() OVER (ORDER BY current_price ASC) AS ranking, id FROM bookmarket_product_register)) AS priority WHERE id=%d", [request.POST['product_id'])

    buyer = request.user
    cursor = connection.cursor()
    if current_price1 >= bid_price :
        return render(request, 'bookmarket/error-price-bid.html')

    cursor.execute("INSERT INTO bookmarket_bid_candidate(bid_date, bid_price, product_id, buyer_id) VALUES (%s, %s, %s, %s)", [bid_date, bid_price, product.id, buyer.id])

    cursor.execute("UPDATE bookmarket_product_register SET current_price = %s WHERE id = %s", [bid_price, product.id])

    cursor.execute("SELECT * FROM bookmarket_product_register")

    row = dictfetchall(cursor)
    context = {"row": row}
    return render(request, 'bookmarket/index.html', context)
