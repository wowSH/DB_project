from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import RegisterForm
from django.db import connection,transaction
import datetime
from django.template import RequestContext
# Create your views here.
from django.utils import timezone
import datetime
# Create your views here.
def index(request):
    return render(request, 'groupbuying/index.html')

def open_new(request):
    if request.method == "POST":

        new_party = Party_Open(
            category = request.POST['category'],
            title = request.POST['title'],
            num_person = request.POST['num_person'],
            content = request.POST['content'],
            closing_date = request.POST['closing_date'],
            image = request.POST['image'],

        )
        new_party.recruiter = request.user
        new_party.open_date = datetime.datetime.now()
        new_party.condition = 'RECRUITING'
        new_party.save()

        return redirect('groupbuying:index')
    else:
        form = RegisterForm()
    return render(request, 'groupbuying/index', {'form': form})

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
        selected_titl =request.POST['selected_title']
        cursor.execute("SELECT * FROM groupbuying_party_open WHERE category = %s AND title LIKE %s",[selected_category,'%'+selected_titl+'%'] )
        row = dictfetchall(cursor)

        context = {"row":row, "selected_category":selected_category}
        return render(request, 'groupbuying/index.html', context)
