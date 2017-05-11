from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import User


#############인덱스###########################################
def index(request):
    sers = User.objects.all()
    str = ""
    for user in sers:
        str += "학번 : {}  이름 : {}<br>비밀번호 : {}<br>이메일 : {}<br>휴대폰 번호 : {}<p>".format(
        user.u_id, user.name, user.passward, user.email,user.HP
        )
    return HttpResponse(str)

###########################################################
def signup(request):

    return

###########################################################
