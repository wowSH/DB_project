from django.conf.urls import include, url
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index),
    url(r'^seek/$', views.seek),
    url(r'^attend/$', views.attend),

]