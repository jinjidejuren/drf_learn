from django.db import models


class Region(models.Model):
    """
    区域
    """
    region_name = models.CharField(verbose_name=u'区域', max_length=64, blank=True, unique=True)
    created_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True, null=True)
    modified_time = models.DateTimeField(verbose_name=u'修改时间', null=True)
    is_delete = models.IntegerField(u'删除', default=0)

    class Meta:
        verbose_name = u'区域'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.region_name


class MachineRoom(models.Model):
    """
    机房
    """
    room_name = models.CharField(verbose_name=u'机房名称', max_length=64, blank=True, unique=True)
    room_code = models.CharField(verbose_name=u'机房编号', max_length=64, blank=True, null=True)
    region_id = models.IntegerField(verbose_name=u'区域id', blank=True)
    created_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True, null=True)
    modified_time = models.DateTimeField(verbose_name=u'修改时间', null=True)
    is_delete = models.IntegerField(u'删除', default=0)

    class Meta:
        verbose_name = u'机房'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.room_name


class Cabinet(models.Model):
    """
    机柜
    """
    cabinet_name = models.CharField(verbose_name=u'机柜名称', max_length=64, blank=True)
    cabinet_code = models.CharField(verbose_name=u'机柜编号', max_length=64, blank=True)
    room_id = models.IntegerField(verbose_name=u'机房id', blank=True)
    created_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True, null=True)
    modified_time = models.DateTimeField(verbose_name=u'修改时间', null=True)
    is_delete = models.IntegerField(u'删除', default=0)

    class Meta:
        verbose_name = u'机柜'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cabinet_name


class Device(models.Model):
    """
    设备
    """
    type_choices = (
        ('storage', '存储设备'),
        ('safe', '安全设备')
    )

    device_name = models.CharField(verbose_name=u'设备名称', max_length=64,
                                   blank=True, unique=True)
    device_type = models.CharField(verbose_name=u'设备类型', max_length=32,
                                   choices=type_choices, blank=True)
    brand = models.CharField(verbose_name=u'品牌', max_length=32, blank=True, null=True)
    model = models.CharField(verbose_name=u'型号', max_length=32, blank=True, null=True)
    hardware = models.TextField(verbose_name=u'硬件信息', blank=True, null=True)
    cabinet_id = models.IntegerField(verbose_name=u'机柜id', blank=True)
    created_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True, null=True)
    modified_time = models.DateTimeField(verbose_name=u'修改时间', null=True)
    is_delete = models.IntegerField(u'删除', default=0)

    class Meta:
        verbose_name = u'设备'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.device_name


class Server(models.Model):
    """
    服务器
    """
    status_choices = (
        ('online', '上线状态'),
        ('offline', '下线状态'),
        ('idle', '闲置状态')
    )

    environment_choices = (
        ('product', '生产环境'),
        ('develop', '开发环境'),
    )

    project = models.CharField(verbose_name=u'项目', max_length=32, blank=True, null=True)
    manager = models.CharField(verbose_name=u'管理者', max_length=32, blank=True, null=True)
    service_tag = models.CharField(verbose_name=u'服务标签', max_length=32, blank=True, null=True)
    server_status = models.CharField(verbose_name=u'服务器状态', max_length=32, choices=status_choices,
                                     blank=True, null=True)
    server_name = models.CharField(verbose_name=u'服务器名称', max_length=64, blank=True, null=True)
    environment = models.CharField(verbose_name=u'', max_length=32, choices=environment_choices, blank=True)
    brand = models.CharField(verbose_name=u'品牌', max_length=32, blank=True, null=True)
    model = models.CharField(verbose_name=u'型号', max_length=32, blank=True, null=True)
    assets_number = models.CharField(verbose_name=u'资产编号', max_length=64, blank=True, null=True)
    ip_addr = models.GenericIPAddressField(verbose_name=u'ip地址', blank=True, null=True)

    cabinet_id = models.IntegerField(verbose_name=u'机柜id', blank=True)
    created_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True, null=True)
    modified_time = models.DateTimeField(verbose_name=u'修改时间', null=True)
    is_delete = models.IntegerField(u'删除', default=0)

    class Meta:
        verbose_name = u'服务器'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.server_name
