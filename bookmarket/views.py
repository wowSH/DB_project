from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import RegisterForm
from django.utils import timezone
import datetime
# Create your views here.
def index(request):
    return render(request, 'bookmarket/index.html')

def register_new(request):
    if request.method == "POST":

        new_product = Product_Register(
            category = request.POST['category'],
            title = request.POST['title'],
            author = request.POST['author'],
            subject = request.POST['subject'],
            imm_price = request.POST['imm_price'],
            init_price = request.POST['init_price'],
            closing_date = request.POST['closing_date'],
            state = request.POST['state'],
            image = request.POST['image'],
            seller = request.user
        )
        new_product.register_date = datetime.datetime.now()

        new_product.save()
        """
        form = RegisterForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.seller = request.user
            post.register_date = timezone.now()
            post.save()
        """
        return redirect('bookmarket:index')
    else:
        form = RegisterForm()
    return render(request, 'bookmarket/index', {'form': form})
