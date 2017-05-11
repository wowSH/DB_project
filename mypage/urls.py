from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^mypage/$', views.index),
    url(r'^mypage/backout/$', views.backout),
    url(r'^mypage/bookmarket/$', views.bookmarket),
    url(r'^mypage/groupbuying/$', views.groupbuying),
    url(r'^mypage/taxipool/$', views.taxipool),
    url(r'^mypage/changeinfo/$', views.changeinfo),

]
