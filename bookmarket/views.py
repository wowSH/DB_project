from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'bookmarket/index.html')

def register(request):
    return render(request, 'bookmarket/register.html')

def bid(request):
    return render(request, 'bookmarket/bid.html')
