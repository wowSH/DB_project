from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns('',
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        name='logout',
        kwargs={'next_page': '/'}
    ),

)