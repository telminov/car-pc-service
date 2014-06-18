# coding: utf-8
from core.utils import json_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
# from rest_framework import viewsets
# from core import serializers
from core import models
# from rest_framework.authentication import BasicAuthentication, SessionAuthentication
# from rest_framework.permissions import IsAuthenticated

@require_POST
@csrf_exempt
@login_required
def add_result(request):
    car = request.user.core_user.car
    value = request.POST['value']
    sensor_pid = request.POST['sensor_pid']
    result_dt = request.POST['result_dt']

    params = {
        'sensor_id': sensor_pid,
        'car': car,
        'value': value,
        'result_dt': result_dt,
    }
    if models.SensorResult.objects.filter(**params).exists():
        return json_response("Already same result exists.")
    else:
        models.SensorResult.objects.create(**params)
        return json_response("Ok")

# class SensorViewSet(viewsets.ReadOnlyModelViewSet):
#     authentication_classes = (SessionAuthentication, )
#     permission_classes = (IsAuthenticated,)
#
#     queryset = models.Sensor.objects.all()
#     serializer_class = serializers.SensorSerializer
#
# class SensorResultViewSet(viewsets.ModelViewSet):
#     authentication_classes = (SessionAuthentication, )
#     permission_classes = (IsAuthenticated,)
#
#     queryset = models.SensorResult.objects.all()
#     serializer_class = serializers.SensorResultSerializer
  