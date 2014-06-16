# coding: utf-8
from rest_framework import viewsets
from core import serializers
from core import models

class SensorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Sensor.objects.all()
    serializer_class = serializers.SensorSerializer

class SensorResultViewSet(viewsets.ModelViewSet):
    queryset = models.SensorResult.objects.all()
    serializer_class = serializers.SensorResultSerializer
  