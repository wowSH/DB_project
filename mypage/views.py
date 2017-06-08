from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import connection, transaction
from bookmarket.models import *
from groupbuying.models import *
from taxipool.models import *

import datetime
# Create your views here.
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
        
        
def changeinfo(request):
    return render(request, 'mypage/changeinfo.html')

def mp_bookmarket(request):
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM bookmarket_bid_candidate")
    biddings = dictfetchall(cursor)
    
    cursor.execute("SELECT bid_price FROM bookmarket_bid_candidate AS b INNER JOIN bookmarket_product_register AS p ON b.product_id = p.id ORDER BY bid_price DESC limit 1")
    highest = dictfetchall(cursor)
    
    rankings = []
    for high,bid in zip(highest, biddings):
        if high['bid_price'] == bid['bid_price']:
            rankings.append(True)
        else:
            rankings.append(False)

    cursor.execute("SELECT p.id AS product_id, b.id AS bid_id, p.title, b.bid_date, b.bid_price, p.category, p.subject, p.imm_price, p.closing_date, p.current_price, p.condition FROM bookmarket_bid_candidate AS b INNER JOIN bookmarket_product_register AS p ON b.product_id = p.id;")
    #cursor.execute("SELECT RANK() OVER (ORDER BY i.bid_price ASC) AS Rank FROM Bid_Candidate AS b INNER JOIN Product_Register AS p ON b.product_id = p.id ")
    bidded_products = dictfetchall(cursor)

    """
    rankings = []    
    for bidding in biddings:
        ordered_list = list(Bid_Candidate.objects.filter(product=bidding.product).order_by('bid_price').values_list('bid_price'))
        ranking = ordered_list.index(bid_price)
        rankings.append(ranking)
    """
    bid_rank_list = zip(rankings, bidded_products)
    
    
    cursor.execute("SELECT * FROM bookmarket_product_register")
    products = dictfetchall(cursor)
    
  
    bid_rank_list = zip(rankings, bidded_products)
    context = {"products": products, "bid_rank_list":bid_rank_list}

    return render(request, 'mypage/bookmarket.html', context)
    
def mp_groupbuying(request):
    return render(request, 'mypage/groupbuying.html')
    
def mp_taxipool(request):
    return render(request, 'mypage/taxipool.html')


    
# def backout (request):
#     return

# def groupbuying(request):
#     return

# def taxipool(request):
#     return

# def bookmarket(request):
#     return
