# coding: utf-8
from rest_framework import viewsets, status
from rest_framework.response import Response
from core import serializers
from core import models

class CarViewSet(viewsets.ModelViewSet):
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer

    def create(self, request, *args, **kwargs):
        if not request.DATA.get('user'):
            # create own user for new car
            car_user = models.User.GenerateCarUser()

            data = request.DATA.copy()
            data['user'] = car_user.id

        # copy/past original create method.
        # can't write
        #   request.DATA = data
        #   return super(CarViewSet, self).create(request, *args, **kwargs)
        # because of can't set attribute for response

        serializer = self.get_serializer(data=data, files=request.FILES)

        if serializer.is_valid():
            self.pre_save(serializer.object)
            self.object = serializer.save(force_insert=True)
            self.post_save(self.object, created=True)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED,
                            headers=headers)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



