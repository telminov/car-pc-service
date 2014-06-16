# coding: utf-8
from django.conf.urls import patterns, url, include
from rest_framework import routers

from core.views.car import CarViewSet

router = routers.DefaultRouter()
router.register('car', CarViewSet)

urlpatterns = patterns('core.views',
    url(r'^', include(router.urls)),
)