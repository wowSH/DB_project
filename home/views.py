from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    msg = "My message"
    return render(request, 'home/index.html', {'message':msg})