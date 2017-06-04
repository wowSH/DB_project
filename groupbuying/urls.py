from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^$', views.index, name="index"),
    url(r'^open/$',views.open, name="open"),
    url(r'^apply/$',views.apply, name="apply"),

]
