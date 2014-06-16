# coding: utf-8
from django.conf.urls import patterns, url, include
from rest_framework import routers

from core.views.car import CarViewSet
from core.views.sensors import SensorViewSet, SensorResultViewSet

router = routers.DefaultRouter()
router.register('car', CarViewSet)
router.register('sensor', SensorViewSet)
router.register('sensor_result', SensorResultViewSet)

urlpatterns = patterns('core.views',
    url(r'^', include(router.urls)),
)