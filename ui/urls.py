# coding: utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('ui.views',
    url(r'^$', 'index.index')
)