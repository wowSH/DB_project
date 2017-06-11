from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.changeinfo, name="changeinfo"),
    url(r'^mp_bookmarket', views.mp_bookmarket, name="mp_bookmarket"),
    url(r'^mp_groupbuying/$', views.mp_groupbuying, name="mp_groupbuying"),
    url(r'^mp_taxipool/$', views.mp_taxipool, name="mp_taxipool"),

    url(r'^bid_detail/$', views.bid_detail, name="bid_detail"),
    url(r'^register_detail/$', views.register_detail, name="register_detail"),

    url(r'^attend_detail/$', views.attend_detail, name="attend_detail"),
    url(r'^seek_detail$', views.seek_detail, name="seek_detail"),

    url(r'^apply_detail/$', views.apply_detail, name="apply_detail"),
    url(r'^open_detail/$', views.open_detail, name="open_detail"),
    # url(r'^backout/$', views.backout, name="backout"),
    # url(r'^bookmarket/$', views.bookmarket, name="bookmarket"),
    # url(r'^groupbuying/$', views.groupbuying, name="groupbuying"),
    # url(r'^taxipool/$', views.taxipool, name="taxipool"),

]
