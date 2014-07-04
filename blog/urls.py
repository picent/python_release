from django.conf.urls import *
from blog.views import archive
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', archive),
)