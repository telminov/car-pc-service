# coding: utf-8
import string
import random

from django.db import models
from django.contrib.auth.models import User as AuthUser

class User(models.Model):
    auth_user = models.OneToOneField(AuthUser, related_name='core_user')
    is_car = models.BooleanField(default=False, help_text=u'Is user a system user account for car pc')

    @classmethod
    def GenerateCarUser(cls):
        def gen_username():
            return ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
        def gen_password():
            return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))

        counter = 0
        while True:
            counter += 1
            # generate random user name
            username = gen_username()
            if AuthUser.objects.filter(username=username).exists():
                if counter > 9000000:
                    raise Exception('Oops!.. Too long name generating. May be all combinations is used? O_o')
                continue

            password = gen_password()
            auth_user = AuthUser.objects.create_user(username, password=password)
            car_user = cls.objects.create(auth_user=auth_user, is_car=True)
            return car_user

    def __unicode__(self):
        return unicode(self.auth_user)

class Car(models.Model):
    user = models.OneToOneField(User, related_name='car')
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=255, blank=True)
