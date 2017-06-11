from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^open$', views.open_new, name='open_new'),
    url(r'^searching$', views.Searching, name='searching'),
    url(r'^applying$', views.applying, name='applying'),
]
