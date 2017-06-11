from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.db import connection, transaction
from django.contrib import messages # error
import datetime
from home.views import *
# Create your views here.
from django.utils import timezone
import datetime

def index(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM taxipool_seek_taxi")
    row = dictfetchall(cursor)
    context = {"row": row}
    return render(request, 'taxipool/index.html', context)

def seek_new(request):
    if request.method == "POST":
        new_taxi = Seek_Taxi(
            content = request.POST['content'],
            num_person = request.POST['num_person'],
            destination = request.POST['destination'],
            departure = request.POST['departure'],
            depart_date = request.POST['depart_date'],
            depart_time = request.POST['depart_time'],
        )
        new_taxi.seeker = request.user
        if new_taxi.num_person > "4" :
            messages.error(request, "People number error : Maximum is 4.")
            return render (request, 'taxipool/index.html')
        register_date = datetime.date.today()
        if str(register_date) > new_taxi.depart_date  :
            messages.error(request, "Date error : Before today.")
            return render (request, 'taxipool/index.html')
        else :
            new_taxi.condition = 'SEEKING'
            new_taxi.save()
            return redirect('taxipool:index')


    else:
        form = RegisterForm()
    return render(request, 'taxipool/index.html', {'form': form})



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
        cursor.execute("SELECT * FROM taxipool_seek_taxi WHERE ('Destination' = %s AND destination LIKE %s) OR ('departure' = %s AND departure LIKE %s)",[selected_category,'%'+selected_titl+'%',selected_category,'%'+selected_titl+'%'] )
        row = dictfetchall(cursor)#

        context = {"row":row, "selected_category":selected_category}
        return render(request, 'taxipool/index.html', context)




@login_required()
def attending(request):
    cursor1 = connection.cursor()
    get_entire_taxipool_with_user(request, cursor1, True)
    if request.POST['condition1'] == "SEEKING":
        attend_date = datetime.datetime.now()
        comment1 = request.POST['comment']
        taxi = Seek_Taxi.objects.get(id=request.POST['taxi_id'])
        num_person1 = request.POST['num_person']
        now_person1 = request.POST['now_person']

        passenger = request.user
        cursor = connection.cursor()
        if num_person1 <= now_person1 :
            messages.error(request, "People number error :It's FULL!")
            return render (request, 'taxipool/index.html')
        cursor.execute("INSERT INTO taxipool_attend_passenger(attend_date, comment, taxi_id, passenger_id) VALUES (%s, %s, %s, %s)", [attend_date, comment1, taxi.id, passenger.id])

        cursor.execute("UPDATE taxipool_seek_taxi SET now_person = now_person+1 WHERE id = %s", [taxi.id])

        cursor.execute("SELECT * FROM taxipool_seek_taxi")
        row = dictfetchall(cursor)
        context = {"row": row}
        return render(request, 'taxipool/index.html', context)
    else :
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM taxipool_seek_taxi")

        row = dictfetchall(cursor)
        context = {"row": row}
        return render(request, 'taxipool/index.html', context)
