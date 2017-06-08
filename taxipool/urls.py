from django.conf.urls import include, url
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^seek$', views.seek_new, name='seek_new'),
    url(r'^searching$', views.Searching, name='Searching'),
    url(r'^attending$', views.attending, name='attending'),
]
