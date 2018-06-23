#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-6-23 下午10:27
# @Author  : zhang chi
# @Site    : 
# @File    : filters.py
# @Software: PyCharm
import django_filters

from .models import *


class ServerFilter(django_filters.rest_framework.FilterSet):
    """
    物理服务器过滤器
    """

    server_name = django_filters.CharFilter(name='server_name', lookup_expr='icontains')
    brand = django_filters.CharFilter(name='brand', lookup_expr='icontains')
    cpus = django_filters.NumberFilter(name='cpus')
    ram = django_filters.NumberFilter(name='ram')
    disk = django_filters.NumberFilter(name='disk')

    class Meta:
        model = Server
        fields = ['server_name', 'brand', 'cpus', 'ram', 'disk', ]
