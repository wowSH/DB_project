from django.conf.urls import include, url
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register_new, name='register_new'),
    url(r'^searching$', views.Searching, name='searching'),
    url(r'^bidding$', views.bidding, name='bidding'),
]
