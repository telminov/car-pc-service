# coding: utf-8
from django.views.decorators.http import require_POST
from rest_framework import viewsets
from core import serializers
from core import models

class CarViewSet(viewsets.ModelViewSet):
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer
