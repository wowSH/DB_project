from django.conf.urls import url
from bookmarket import views
 
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register', views.register),
    url(r'^bid', views.bid),
]