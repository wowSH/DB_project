from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import RegisterForm
from django.db import connection,transaction
import datetime
from django.template import RequestContext
# Create your views here.
from django.utils import timezone
# Create your views here.
def index(request):
    return render(request, 'taxipool/index.html')

def seek_new(request):
    if request.method == "POST":
        new_taxi = Seek_Taxi(
            content = request.POST['content'],
            num_person = request.POST['num_person'],
            destination = request.POST['destination'],
            departure = request.POST['departure'],
            depart_date = request.POST['depart_date'],
            depart_time = request.POST['depart_time'],
            seeker = request.user
        )
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
