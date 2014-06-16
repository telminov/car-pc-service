# coding: utf-8
from django.db import models
from django.contrib.auth.models import User as AuthUser

class User(models.Model):
    auth_user = models.OneToOneField(AuthUser, related_name='core_user')
    is_car = models.BooleanField(default=False, help_text=u'Is user a system user account for car pc')

    def __unicode__(self):
        return unicode(self.auth_user)

class Car(models.Model):
    user = models.OneToOneField(User, related_name='car')
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=255, blank=True)
