#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-5-23 下午10:36
# @Author  : zhang chi
# @Site    : 
# @File    : serializers.py
# @Software: PyCharm
from rest_framework import serializers
from .models import *


class RegionSerializer(serializers.ModelSerializer):
    """
    区域序列化
    """

    class Meta:
        model = Region
        fields = ('id', 'region_name', 'created_time', 'modified_time')


class MachineRoomSerializer(serializers.ModelSerializer):
    """
    机房序列化
    """

    class Meta:
        model = MachineRoom
        fields = ('id', 'room_name', 'room_code', 'region_id',
                  'created_time', 'modified_time')


class CabinetSerializer(serializers.ModelSerializer):
    """
    机柜序列化
    """

    class Meta:
        model = Cabinet
        fields = ('id', 'cabinet_name', 'cabinet_code', 'room_id',
                  'created_time', 'modified_time')


class DeviceSerializer(serializers.ModelSerializer):
    """
    设备序列化
    """

    class Meta:
        model = Device
        fields = ('id', 'device_name', 'device_type', 'brand', 'model',
                  'hardware', 'cabinet_id', 'created_time', 'modified_time')


class ServiceSerializer(serializers.ModelSerializer):
    """
    服务器序列化
    """

    class Meta:
        model = Server
        fields = ('id', 'project', 'manager', 'service_tag', 'server_status', 'server_name',
                  'environment', 'brand', 'model', 'assets_number', 'ip_addr', 'cabinet_id')
