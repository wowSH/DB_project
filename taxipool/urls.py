from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^$', views.index, name="index"),
    url(r'^seek/$', views.seek, name="seek"),
    url(r'^attend/$', views.attend, name="attend"),

]
