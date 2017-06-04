# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from bookmarket import views


urlpatterns = [

    url(r'^$', views.index, name="index"), #인덱스
    url(r'^register/$', views.register, name="register"), #등록창
    url(r'^bid/$', views.bid, name="bid"), #입찰창

]
