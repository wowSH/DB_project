# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from bookmarket import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name="index"), #인덱스
    url(r'^register/$',views.register), #등록창
    url(r'^bid/$',views.bid), #입찰창

]
