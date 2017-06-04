from django.conf.urls import url
from bookmarket import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register_new, name='register_new'),
]