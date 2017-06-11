from django.shortcuts import render, redirect
from django.http import HttpResponse
from bookmarket.models import *
from groupbuying.models import *
from taxipool.models import *
from django.contrib.auth.decorators import login_required
from django.db import connection, transaction
import sys
import datetime

# Create your views here.
def index(request):
    #return HttpResponse("<h1>Hello, World!</h1>")
    return render(request, 'home/index.html')

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def get_entire_bookmarket_with_user(request, cursor, with_user=False):

    time_now = datetime.datetime.now()
    cursor.execute("UPDATE bookmarket_product_register SET condition = 'SSUCC' WHERE %s > closing_date AND current_price >= imm_price",[time_now])
    cursor.execute("UPDATE bookmarket_product_register SET condition = 'SFAIL' WHERE %s > closing_date AND current_price < imm_price",[time_now])


    if with_user: # user-specific
        cursor.execute("SELECT p.*, p.id as product_id, groupb.*, groupb.id as bid_id FROM bookmarket_product_register AS p INNER JOIN  (SELECT b2.*, MAX(b2.bid_price) FROM bookmarket_bid_candidate AS b2 GROUP BY b2.product_id) AS groupb ON p.id = groupb.product_id AND groupb.buyer_id = %s", [request.user.id])
    else:
        cursor.execute("SELECT p.*, p.id as product_id, groupb.*, groupb.id as bid_id FROM bookmarket_product_register AS p INNER JOIN  (SELECT b2.*, MAX(b2.bid_price) FROM bookmarket_bid_candidate AS b2 GROUP BY b2.product_id) AS groupb ON p.id = groupb.product_id")



    bidded_products = dictfetchall(cursor)

    cursor.execute("SELECT p.* FROM bookmarket_product_register as p WHERE p.seller_id = %s", [request.user.id])
    products = dictfetchall(cursor)

    context = {"products": products, "bidded_products":bidded_products}
    return context


def get_product_curr_price(request, cursor, product_id):
    cursor.execute("SELECT current_price FROM bookmarket_product_register WHERE id = %s", [product_id])
    curr_price = cursor.fetchone()[0]
    return curr_price


def get_product_id_from_bid_id(request, cursor, bid_id):
    cursor.execute("SELECT product_id FROM bookmarket_bid_candidate WHERE id = %s", [bid_id])
    product_id = cursor.fetchone()[0]
    return product_id


def update_product(request, cursor, product_id):
    cursor.execute("SELECT MAX(b.bid_price) FROM bookmarket_bid_candidate as b INNER JOIN bookmarket_product_register as p ON p.id = b.product_id AND p.id = %s", [product_id])
    max_bid_price = cursor.fetchone()[0]
    curr_price = get_product_curr_price(request, cursor, product_id)

    if max_bid_price > curr_price:
        curr_price = max_bid_price
        cursor.execute("UPDATE bookmarket_product_register SET current_price = %s WHERE id = %s", [curr_price, product_id])
    return

def close_product(request, cursor, product_id):
    cursor.execute("SELECT Count(*) FROM bookmarket_product_register WHERE id = %s", product_id)
    num_row = int(cursor.fetchone()[0])

    cursor.execute("UPDATE bookmarket_product_register SET condition = %s WHERE id = %s", ["SSUCC", product_id])
    return

def delete_product(request, cursor, product_id):
    cursor.execute('DELETE FROM bookmarket_product_register WHERE id = %s', [product_id])
    return


def update_bid(request, cursor, bid_id, new_price):
    cursor.execute("UPDATE bookmarket_bid_candidate SET bid_price = %s WHERE id = %s", [new_price, bid_id])

    product_id = get_product_id_from_bid_id(request, cursor, bid_id)
    curr_price = get_product_curr_price(request, cursor, product_id)
    if new_price > str(curr_price):
        cursor.execute("UPDATE bookmarket_product_register SET current_price = %s WHERE id = %s", [new_price, product_id])
    return


def delete_bid(request, cursor, bid_id):
    try:
        cursor.execute('DELETE FROM bookmarket_bid_candidate WHERE id = %s', [bid_id])

        product_id = get_product_id_from_bid_id(request, cursor, bid_id)
        curr_price = get_product_curr_price(request, cursor, product_id)

        cursor.execute("SELECT product_id FROM bookmarket_bid_candidate WHERE id = %s", [bid_id])
        product_id = cursor.fetchone()[0]
        update_product(request, cursor, product_id)
    except:
        pass
    return




def get_entire_taxipool_with_user(request, cursor, with_user=False):
    #date_now = datetime.date.today()
    time_now = datetime.date.today()
    cursor.execute("UPDATE taxipool_seek_taxi SET condition = 'SSUCC' WHERE %s > depart_date AND now_person >= num_person",[time_now])
    cursor.execute("UPDATE taxipool_seek_taxi SET condition = 'SFAIL' WHERE %s > depart_date  AND now_person < num_person",[time_now])

    if with_user: # user-specific
        cursor.execute("SELECT s.*, s.id as seek_id, a.*, a.id as attend_id FROM taxipool_seek_taxi as s INNER JOIN taxipool_attend_passenger AS a ON a.taxi_id = s.id AND a.passenger_id = %s", [request.user.id])
    else:
        cursor.execute("SELECT s.*, s.id as seek_id, a.*, a.id as attend_id FROM taxipool_seek_taxi as s INNER JOIN taxipool_attend_passenger AS a ON a.taxi_id = s.id")
    attended_taxis = dictfetchall(cursor)

    cursor.execute("SELECT s.* FROM taxipool_seek_taxi as s WHERE s.seeker_id = %s", [request.user.id])
    sought_taxis = dictfetchall(cursor)

    context = {"sought_taxis": sought_taxis, "attended_taxis":attended_taxis}
    return context

def delete_seek(request, cursor, seek_id):
    cursor.execute('DELETE FROM taxipool_seek_taxi WHERE id = %s', [seek_id])
    return

def get_seek_id_from_attend_id(request, cursor, attend_id):
    cursor.execute("SELECT taxi_id FROM taxipool_attend_passenger WHERE id = %s", [attend_id])
    seek_id = cursor.fetchone()[0]
    return seek_id


def delete_attend(request, cursor, attend_id):
    try:
        seek_id = get_seek_id_from_attend_id(request, cursor, attend_id)
        cursor.execute('DELETE FROM taxipool_attend_passenger WHERE id = %s', [attend_id])
        # decrement now person
        cursor.execute("UPDATE taxipool_seek_taxi SET now_person = now_person-1 WHERE id = %s", [seek_id])
    except:
        pass
    return


def get_entire_groupbuying_with_user(request, cursor, with_user=False):
    time_now = datetime.datetime.now()
    cursor.execute("UPDATE groupbuying_party_open SET condition = 'SSUCC' WHERE %s > closing_date AND now_person >= num_person",[time_now])
    cursor.execute("UPDATE groupbuying_party_open SET condition = 'SFAIL' WHERE %s > closing_date AND now_person < num_person",[time_now])


    if with_user: # user-specific
        cursor.execute("SELECT p.*, p.id as party_id, a.*, a.id as apply_id FROM groupbuying_party_open AS p INNER JOIN groupbuying_apply_applicant AS a ON a.party_id = p.id AND a.applicant_id = %s", [request.user.id])
    else:
        cursor.execute("SELECT p.*, p.id as party_id, a.*, a.id as apply_id FROM groupbuying_party_open AS p INNER JOIN groupbuying_apply_applicant AS a ON a.party_id = p.id")
    applied_parties = dictfetchall(cursor)

    cursor.execute("SELECT p.* FROM groupbuying_party_open as p WHERE p.recruiter_id = %s", [request.user.id])
    opened_parties = dictfetchall(cursor)

    context = {"applied_parties": applied_parties, "opened_parties":opened_parties}
    return context

def get_party_id_from_apply_id(request, cursor, apply_id):
    cursor.execute("SELECT party_id FROM groupbuying_apply_applicant WHERE id = %s", [apply_id])
    party_id = cursor.fetchone()[0]
    return party_id

def update_apply(request, cursor, apply_id, content):
    cursor.execute("UPDATE groupbuying_apply_applicant SET content = %s WHERE id = %s", [content, apply_id])
    return

def delete_apply(request, cursor, apply_id):
    try:
        party_id = get_party_id_from_apply_id(request, cursor, apply_id)
        cursor.execute("DELETE FROM groupbuying_apply_applicant WHERE id = %s", [apply_id])
        cursor.execute("UPDATE groupbuying_party_open SET now_person = now_person-1 WHERE id = %s", [party_id])
    except:
        pass
    return

def delete_open(request, cursor, open_id):
    cursor.execute('DELETE FROM groupbuying_party_open WHERE id = %s', [open_id])
    return
