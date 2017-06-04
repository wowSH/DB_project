from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name = 'index'),
    url(r'^backout/$', views.backout),
    url(r'^bookmarket/$', views.bookmarket),
    url(r'^groupbuying/$', views.groupbuying),
    url(r'^taxipool/$', views.taxipool),
    url(r'^changeinfo/$', views.changeinfo),

]
