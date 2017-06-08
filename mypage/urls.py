from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.changeinfo, name="changeinfo"),
    url(r'^mp_bookmarket', views.mp_bookmarket, name="mp_bookmarket"),
    url(r'^mp_groupbuying/$', views.mp_groupbuying, name="mp_groupbuying"),
    url(r'^mp_taxipool/$', views.mp_taxipool, name="mp_taxipool"),
    
    # url(r'^detail/$', views.detail, name="detail"),
    
    # url(r'^backout/$', views.backout, name="backout"),
    # url(r'^bookmarket/$', views.bookmarket, name="bookmarket"),
    # url(r'^groupbuying/$', views.groupbuying, name="groupbuying"),
    # url(r'^taxipool/$', views.taxipool, name="taxipool"),

]