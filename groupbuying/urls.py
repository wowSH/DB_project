from django.conf.urls import include, url
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^groupbuying/$', views.index),
    url(r'^groupbuying/open$',views.open),
    url(r'^groupbuying/apply$',views.apply),

]
