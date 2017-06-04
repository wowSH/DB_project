from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import RegisterForm
from django.utils import timezone
import datetime
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

        new_taxi.save()

        return redirect('taxipool:index')
    else:
        form = RegisterForm()
    return render(request, 'taxipool/index', {'form': form})
