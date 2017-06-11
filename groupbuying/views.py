from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.db import connection, transaction
from home.views import * # common fucntion
from django.contrib import messages # error
import datetime

# Create your views here.
from django.utils import timezone
import datetime

# Create your views here.
def index(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM groupbuying_party_open")
    row = dictfetchall(cursor)
    context = {"row": row}
    return render(request, 'groupbuying/index.html', context)

def open_new(request):
    if request.method == "POST":
        new_party = Party_Open(
                category = request.POST['category'],
                title = request.POST['title'],
                num_person = request.POST['num_person'],
                content = request.POST['content'],
                closing_date = request.POST['closing_date'],
                image = request.FILES['image'],
                )
        new_party.recruiter = request.user
        new_party.open_date = str(datetime.datetime.now())
        if new_party.open_date > new_party.closing_date:
            messages.error(request, "Date error : Before today.")
            return render (request, 'groupbuying/index.html')
        else :
            new_party.condition = 'RECRUITING'
            new_party.save()
            return redirect('groupbuying:index')
    else:
        form = RegisterForm()
    return render(request, 'groupbuying/index.html', {'form': form})

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


@login_required()
def applying(request):
    cursor1 = connection.cursor()
    get_entire_groupbuying_with_user(request, cursor1, True)
    if request.POST['condition1'] == "RECRUITING":
        apply_date = datetime.datetime.now()
        comment1 = request.POST['comment']
        party = Party_Open.objects.get(id=request.POST['party_id'])
        num_person1 = request.POST['num_person']
        now_person1 = request.POST['now_person']

        applicant = request.user
        cursor = connection.cursor()
        if num_person1 <= now_person1 :
            messages.error(request, "People number error : It's FULL!")
            return render (request, 'groupbuying/index.html')

        cursor.execute("INSERT INTO groupbuying_apply_applicant(apply_date, comment, party_id, applicant_id) VALUES (%s, %s, %s, %s)", [apply_date, comment1, party.id, applicant.id])

        cursor.execute("UPDATE groupbuying_party_open SET now_person = now_person+1 WHERE id = %s", [party.id])

        cursor.execute("SELECT * FROM groupbuying_party_open")
        row = dictfetchall(cursor)
        context = {"row": row}
        return render(request, 'groupbuying/index.html', context)
    else :
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM groupbuying_party_open")

        row = dictfetchall(cursor)
        context = {"row": row}
        return render(request, 'groupbuying/index.html', context)
