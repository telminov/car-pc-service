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



# http://en.wikipedia.org/wiki/OBD-II_PIDs
class Sensor(models.Model):
    description = models.CharField(max_length='255', unique=True)
    pid = models.CharField(max_length='2', unique=True)
    unit = models.CharField(max_length='10', blank=True)

    class Meta:
        ordering = ('id', )

    def __unicode__(self):
        return self.description

class SensorResult(models.Model):
    sensor = models.ForeignKey(Sensor, to_field='pid', related_name='results', db_index=True)
    car = models.ForeignKey(Car, related_name='results', db_index=True)
    value = models.CharField(max_length='50')
    dc = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        get_latest_by = 'dc'

    def __unicode__(self):
        return '%s - %s' % (self.sensor_id, self.value)