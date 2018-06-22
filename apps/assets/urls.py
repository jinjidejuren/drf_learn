#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-5-27 下午5:43
# @Author  : zhang chi
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url, include
from rest_framework import routers
from apps.assets import views

router = routers.DefaultRouter()
router.register(r'regions', views.RegionViewSet, base_name='regions')
router.register(r'machine_rooms', views.MachineRoomViewSet, base_name='machine_rooms')
router.register(r'cabinets', views.CabinetViewSet, base_name='cabinets')
router.register(r'devices', views.DeviceViewSet, base_name='devices')


urlpatterns = [
    url(r'^', include(router.urls))
]