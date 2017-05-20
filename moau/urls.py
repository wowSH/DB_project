"""moau URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
<<<<<<< HEAD
from django.conf.urls import url
from django.contrib import admin
from home import views
=======
from django.conf.urls import url, include
from django.contrib import admin
from home import views
from bookmarket import urls as bookmarket_urls
>>>>>>> 915f5a3d9763ebad898384496d8127b3b72f362a

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
<<<<<<< HEAD
=======
    url(r'^bookmarket/', include(bookmarket_urls)),
>>>>>>> 915f5a3d9763ebad898384496d8127b3b72f362a
]
