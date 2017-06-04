from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Create your views here.
def changeinfo(request):
    return render(request, 'mypage/changeinfo.html')

def mp_bookmarket(request):
    return render(request, 'mypage/bookmarket.html')
    
def mp_groupbuying(request):
    return render(request, 'mypage/groupbuying.html')
    
def mp_taxipool(request):
    return render(request, 'mypage/taxipool.html')


# def backout (request):
#     return

# def groupbuying(request):
#     return

# def taxipool(request):
#     return

# def bookmarket(request):
#     return
