from django.conf.urls import include, url
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^account/', views.index),#기본 페이지

    url(r'^account/signup/$',views.signup)#회원가입 페이지

]
