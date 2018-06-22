from rest_framework import viewsets
from rest_framework import permissions

from .serializers import *
from .paginations import *


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
