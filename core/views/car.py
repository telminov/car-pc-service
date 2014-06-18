# coding: utf-8
import string
import random
from core.utils import json_response
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
# from rest_framework import viewsets
# from core import serializers
from core import models
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import IsAuthenticated

@require_POST
@csrf_exempt
@login_required
def create(request):
    user_name = _gen_username()
    password = _gen_password()
    car_name = request.POST['name']
    car_description = request.POST.get('description', '')

    if models.Car.objects.filter(
        name=car_name,
        user__main_user__auth_user=request.user
    ).exists():
        err_msg = 'Car with name "%s" for user "%s" already exists.' % (car_name, request.user)
        return json_response({'error': err_msg}, status=400)

    auth_user = AuthUser.objects.create_user(username=user_name, password=password)
    user = models.User.objects.create(auth_user=auth_user, is_car=True, main_user=request.user.core_user)
    models.Car.objects.create(user=user, name=car_name, description=car_description)

    result = {
        'user_name': user_name,
        'password': password,
    }

    return json_response(result)


def _gen_username():
    for i in xrange(0, 100500):
        user_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
        if not AuthUser.objects.filter(username=user_name).exists():
            return user_name
    raise Exception('Oops!.. Too long name generating. May be all combinations is used? O_o')

def _gen_password():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))

# class CarViewSet(viewsets.ModelViewSet):
#     authentication_classes = (SessionAuthentication, )
#     permission_classes = (IsAuthenticated,)
#
#     queryset = models.Car.objects.all()
#     serializer_class = serializers.CarSerializer



