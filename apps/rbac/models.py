from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from ldap3 import Server, Connection, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES
from ldap3.core.exceptions import LDAPKeyError

from settings import base


class UserProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField(verbose_name="姓名", max_length=64, null=True, blank=True)
    password = models.CharField(verbose_name="密码", max_length=64, null=True, blank=True)
    first_name = models.CharField(verbose_name="姓氏", max_length=64, null=True, blank=True)
    last_name = models.CharField(verbose_name="名字", max_length=64, null=True, blank=True)
    email = models.EmailField(verbose_name="邮箱", max_length=100, null=True, blank=True)
    mobile = models.CharField(verbose_name="电话", max_length=11, null=True, blank=True)
    wechat = models.CharField(verbose_name="微信", max_length=32, null=True, blank=True)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True, blank=True, null=True)

    @property
    def name(self):
        return self.last_name + self.first_name

    class Meta(AbstractUser.Meta):
        db_table = 'rbac_users'
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def check_password(self, raw_password):
        base_cn = "dc=guahao-inc,dc=com"  # 基本信息
        server = Server(base.LOGIN_LDAP_SERVER)
        conn = Connection(server, user=base.LOGIN_LDAP_USER, password=base.LOGIN_LDAP_PASSWD)
        conn.bind()
        conn.search('ou=people,' + base_cn, '(&(uid=' + str(self.username) + ')(objectclass=person))',
                    attributes=[ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES])

        if hasattr(conn, 'entries') and conn.entries:
            ens = conn.entries
        else:
            ens = []
        conn.unbind()
        if ens:
            self.user_info_from_ldap = ens[0]
            pwd = ens[0]['userPassword']
            # self.first_name = self.user_info_from_ldap['displayName']
            # self.last_name = self.user_info_from_ldap['givenName']
            # self.email = self.user_info_from_ldap['mail']
            if pwd.value.decode() == raw_password:
                return True
        return False

    @receiver(post_save, sender=base.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

    @classmethod
    def get_obj_or_new(cls, username):
        """
        查询数据库是否存在，有就返回，没有就创建一个EUserModel
        :param username: 用户名
        :return:
        """
        try:
            e = cls.objects.get_by_natural_key(username=username)
        except ObjectDoesNotExist:
            e = None
        if e:
            return e
        return cls(username=username)

    @classmethod
    def sync_info_from_ldap(self):
        if self.user_info_from_ldap:
            try:
                self.first_name = (lambda x: x if x != "[]" else "")(self.user_info_from_ldap['displayName'])
            except LDAPKeyError:
                self.first_name = ""
            try:
                self.last_name = (lambda x: x if x != "[]" else "")(self.user_info_from_ldap['givenName'])
            except LDAPKeyError:
                self.last_name = ""
            try:
                self.email = (lambda x: x if x != "[]" else "")(self.user_info_from_ldap['mail'])
            except LDAPKeyError:
                self.email = ""

    def __str__(self):
        return self.username
