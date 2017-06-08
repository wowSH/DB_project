from django.shortcuts import render, redirect
from django.http import HttpResponse
from bookmarket.models import *
from groupbuying.models import *
from taxipool.models import *
from django.contrib.auth.decorators import login_required
from django.db import connection, transaction
from home.views import * # common fucntion

import datetime
# Create your views here.

def changeinfo(request):
    return render(request, 'mypage/changeinfo.html')

def mp_bookmarket(request):
    cursor = connection.cursor()
    context = get_entire_bookmarket_with_user(request, cursor, True)
    return render(request, 'mypage/bookmarket.html', context)

def mp_groupbuying(request):
    cursor = connection.cursor()
    context = get_entire_groupbuying_with_user(request, cursor, True)
    return render(request, 'mypage/groupbuying.html',context)

def mp_taxipool(request):
    cursor = connection.cursor()
    context = get_entire_taxipool_with_user(request, cursor, True)
    return render(request, 'mypage/taxipool.html',context)

def bid_detail(request):
    new_bid_price = request.POST['new_bid_price1']
    bid_id = request.POST['bid_id']
    product_id = request.POST['product_id']

    cursor = connection.cursor()
    if request.POST.get('new_bid'):
        update_bid(request, cursor, bid_id, new_bid_price)

    if request.POST.get('delete'):
        delete_bid(request, cursor, bid_id)

    # common
    context = get_entire_bookmarket_with_user(request, cursor, True)
    return render(request, 'mypage/bookmarket.html', context)

def register_detail(request):
    product_id = request.POST['product_id']

    cursor = connection.cursor()
    if request.POST.get('closing'):
        close_product(request, cursor, product_id)

    if request.POST.get('delete'):
        delete_product(request, cursor, product_id)

    context = get_entire_bookmarket_with_user(request, cursor, True)
    return render(request, 'mypage/bookmarket.html', context)
# def backout (request):


def seek_detail(request):
    seek_id = request.POST['seek_id']

    cursor = connection.cursor()
    if request.POST.get('delete'):
        delete_seek(request, cursor, seek_id)

    context = get_entire_taxipool_with_user(request, cursor, True)
    return render(request, 'mypage/taxipool.html', context)

def attend_detail(request):
    attend_id = request.POST['attend_id']

    cursor = connection.cursor()
    if request.POST.get('delete'):
        delete_attend(request, cursor, attend_id)

    context = get_entire_taxipool_with_user(request, cursor, True)
    return render(request, 'mypage/taxipool.html', context)

def apply_detail(request):
    apply_id = request.POST['apply_id']
    content = request.POST['content']

    cursor = connection.cursor()
    if request.POST.get('change'):
        update_apply(request, cursor, apply_id, content)

    if request.POST.get('delete'):
        delete_apply(request, cursor, apply_id)

    context = get_entire_groupbuying_with_user(request, cursor, True)
    return render(request, 'mypage/groupbuying.html', context)

def open_detail(request):
    open_id = request.POST['open_id']
    cursor = connection.cursor()
    if request.POST.get('delete'):
        delete_open(request, cursor, open_id)

    context = get_entire_groupbuying_with_user(request, cursor, True)
    return render(request, 'mypage/groupbuying.html', context)
