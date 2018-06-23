from rest_framework import viewsets
from rest_framework import permissions
from django_filters import rest_framework
from rest_framework import filters


from .serializers import *
from .paginations import *
from .filters import *


class CustomerAccessPermission(permissions.BasePermission):
    """
    自定义权限控制
    """
    def has_permission(self, request, view):
        method = request.method
        if method == "GET":
            return True
        elif method == "POST":
            print("post is allow!")
            return True
        else:
            print("other method is allow!")
            return True


class RegionViewSet(viewsets.ModelViewSet):
    """
    区域操作视图
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    pagination_class = MyFormatResultsSetPagination
    permission_classes = (CustomerAccessPermission, )


class MachineRoomViewSet(viewsets.ModelViewSet):
    """
    机房操作视图
    """
    queryset = MachineRoom.objects.all()
    serializer_class = MachineRoomSerializer
    pagination_class = StandardResultsSetPagination


class CabinetViewSet(viewsets.ModelViewSet):
    """
    机柜操作视图
    """
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer
    pagination_class = LargeResultsSetPagination


class DeviceViewSet(viewsets.ModelViewSet):
    """
    设备操作视图
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    pagination_class = LargeResultsSetPagination


class ServerViewSet(viewsets.ModelViewSet):
    """
    物理服务器视图
    """
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    pagination_class = MyFormatResultsSetPagination
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, )
    filter_class = ServerFilter
    search_fields = ('^server_name', '=brand', 'status', )
    ordering_fields = ('cpus', 'ram', 'disk', 'product_date', )
    ordering = ('-created_time', )
