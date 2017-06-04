
from django.conf.urls import url, include
from django.contrib import admin
from home import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url('', include('social_django.urls', namespace='social')),
    url(r'^home/', include('home.urls', namespace="home")),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

    url(r'^bookmarket/', include('bookmarket.urls', namespace="bookmarket")),
    url(r'^groupbuying/', include('groupbuying.urls', namespace="groupbuying") ),
    url(r'^taxipool/', include('taxipool.urls', namespace="taxipool") ),
    url(r'^mypage/', include('mypage.urls', namespace="mypage")),
]
