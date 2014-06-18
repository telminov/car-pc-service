# coding: utf-8
from django.contrib import admin
from core import models

class UserAdmin(admin.ModelAdmin):
    list_display = ('auth_user', 'is_car')
admin.site.register(models.User, UserAdmin)

class CarAdmin(admin.ModelAdmin):
    list_display = ('name', )
admin.site.register(models.Car, CarAdmin)