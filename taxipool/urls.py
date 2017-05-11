from django.conf.urls import include, url
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^taxipool/$', views.index),
    url(r'^taxipool/seek/$', views.seek),
    url(r'^taxipool/attend/$', views.attend),

]
