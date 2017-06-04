
from django.conf.urls import url, include
from django.contrib import admin
from home import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url('', include('social_django.urls', namespace='social')),
    url(r'^home/', include('home.urls')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

    url(r'^bookmarket/', include('bookmarket.urls')),
    url(r'^groupbuying/', include('groupbuying.urls')),
    url(r'^taxipool/', include('taxipool.urls')),
    url(r'^mypage/', include('mypage.urls')),
]
