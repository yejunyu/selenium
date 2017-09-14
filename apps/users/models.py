# -*- coding: utf-8 -*-

from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"手机")
    image = models.ImageField(upload_to="media/userprofile/%Y", default="media/default.jpg", max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    user_name = models.ForeignKey(UserProfile, verbose_name=u"用户",default=1)
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(verbose_name=u"发送类型", choices=(("register", u"注册"), ("foget", u"找回密码")), max_length=10, default='register')
    send_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.now)  # 这里不能加括号,加了默认时间都会是model创建的时间

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code,self.email)


class EmailBox(models.Model):
    user_name = models.ForeignKey(UserProfile, verbose_name=u"用户", default=1)
    title = models.CharField(max_length=100, verbose_name=u"标题")
    content = models.TextField(verbose_name=u"内容")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=u"创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name=u"修改时间")


    class Meta:
        verbose_name = u"收件箱"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}({1})".format(self.title,self.user_name.username)