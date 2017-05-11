from django.conf.urls import include, url
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^bookmarket/$', views.index),#인덱스
    url(r'^bookmarket/register/$',views.register),#등록창
    url(r'^bookmarket/bid/$',views.bid),#입찰창


]
