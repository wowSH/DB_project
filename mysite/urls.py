from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('home.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^bookmarket/', include('bookmarket.urls')),
    url(r'^groupbuying/', include('groupbuying.urls')),
    url(r'^taxipool/', include('taxipool.urls')),
    url(r'^mypage/', include('mypage.urls')),


]
