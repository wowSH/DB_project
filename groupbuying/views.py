from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import RegisterForm
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
            recruiter = request.user
        )
        new_party.open_date = datetime.datetime.now()

        new_party.save()

        return redirect('groupbuying:index')
    else:
        form = RegisterForm()
    return render(request, 'groupbuying/index', {'form': form})
