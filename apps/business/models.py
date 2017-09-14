# -*- coding: utf-8 -*-
import datetime

from django.db import models
from users.models import UserProfile
from browser.models import ClickTask

# Create your models here.
'''
CPM业务
'''
class CPMWork(models.Model):
    user_name = models.ForeignKey(UserProfile, verbose_name=u"任务发布人", default=1)
    task_id = models.ForeignKey(ClickTask, verbose_name=u'任务ID')
    url = models.CharField(max_length=500, verbose_name=u"投放链接")
    click_nums = models.PositiveIntegerField(default=0, verbose_name=u"投定量")
    ip_nums = models.PositiveIntegerField(default=0, verbose_name=u"已投放IP")
    pv_nums = models.PositiveIntegerField(default=0, verbose_name=u"已投放PV")
    is_control = models.PositiveSmallIntegerField(choices=((0,"否"),(1,"是")), default=0, verbose_name=u"是否控量")
    status = models.PositiveSmallIntegerField(choices=((0,'未开始'),(1,'正在执行'),(2,'完成'),(3,'任务暂停')), default=0, verbose_name=u"状态")
    remark = models.CharField(max_length=255, verbose_name=u"备注", null=True, blank=True)
    task_time = models.DateField(default=datetime.date.today, verbose_name=u"投放时间")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = u"CPM业务"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}:{}".format(self.user_name.username, self.task_id.id)


'''
CPC业务
'''
class CPCWork(models.Model):
    user_name = models.ForeignKey(UserProfile, verbose_name=u"任务发布人", default=1)
    task_id = models.ForeignKey(ClickTask, verbose_name=u'任务ID')
    url = models.CharField(max_length=500, verbose_name=u"投放链接")
    click_nums = models.PositiveIntegerField(default=0, verbose_name=u"投定量")
    hasclicked = models.PositiveIntegerField(default=0, verbose_name=u"已投放点击量")
    ip_nums = models.PositiveIntegerField(default=0, verbose_name=u"已投放IP")
    is_control = models.PositiveSmallIntegerField(choices=((0,"否"),(1,"是")), default=0, verbose_name=u"是否控量")
    status = models.PositiveSmallIntegerField(default=0, verbose_name=u"状态")
    remark = models.CharField(max_length=255, verbose_name=u"备注", null=True, blank=True)
    task_time = models.DateField(default=datetime.date.today, verbose_name=u"投放时间")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # click_detail = models.ForeignKey(verbose_name=u"投放明细")


    class Meta:
        verbose_name = u"CPC业务"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}:{}".format(self.user_name.username,self.task_id)


'''
排名业务
'''
class RankWork(models.Model):
    user_name = models.ForeignKey(UserProfile, verbose_name=u"任务发布人", default=1)
    task_id = models.ForeignKey(ClickTask, verbose_name=u'任务ID')
    url = models.CharField(max_length=500, verbose_name=u"投放链接")
    click_nums = models.PositiveIntegerField(default=0, verbose_name=u"投定量")
    hasclicked = models.PositiveIntegerField(default=0, verbose_name=u"已投放点击量")
    ip_nums = models.PositiveIntegerField(default=0, verbose_name=u"已投放IP")
    is_control = models.PositiveSmallIntegerField(choices=((0,"否"),(1,"是")), default=0, verbose_name=u"是否控量")
    status = models.PositiveSmallIntegerField(default=0, verbose_name=u"状态")
    remark = models.CharField(max_length=255, verbose_name=u"备注", null=True, blank=True)
    task_time = models.DateField(default=datetime.date.today, verbose_name=u"投放时间")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # click_detail = models.ForeignKey(verbose_name=u"投放明细")


    class Meta:
        verbose_name = u"排名业务"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_name.username+":"+self.task_id.id


'''
CPM历史数据
'''
class CPMHistory(models.Model):
    user_name = models.ForeignKey(UserProfile, verbose_name=u"任务发布人", default=1)
    task_id = models.ForeignKey(ClickTask, verbose_name=u'任务ID')
    url = models.CharField(max_length=500, verbose_name=u"投放链接")
    click_nums = models.PositiveIntegerField(default=0, verbose_name=u"投定量")
    ip_nums = models.PositiveIntegerField(default=0, verbose_name=u"已投放IP")
    pv_nums = models.PositiveIntegerField(default=0, verbose_name=u"已投放PV")
    history = models.ForeignKey(CPMWork, verbose_name=u"历史")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = u"CPM历史数据"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_name.username+":"+self.task_id


'''
CPC历史数据
'''
class CPCHistory(models.Model):
    user_name = models.ForeignKey(UserProfile, verbose_name=u"任务发布人", default=1)
    task_id = models.ForeignKey(ClickTask, verbose_name=u'任务ID')
    url = models.CharField(max_length=500, verbose_name=u"投放链接")
    click_nums = models.PositiveIntegerField(default=0, verbose_name=u"投定量")
    ip_nums = models.PositiveIntegerField(default=0, verbose_name=u"已投放IP")
    pv_nums = models.PositiveIntegerField(default=0, verbose_name=u"已投放PV")
    history = models.ForeignKey(CPCWork, verbose_name=u"历史")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = u"CPC历史数据"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_name.username+":"+self.task_id


'''
多URL列表
url以;分隔
({权重},{url})
10,http://www.baidu.com;
20,http://www.google.com;
'''
class Urls(models.Model):
    user_name = models.ForeignKey(UserProfile, verbose_name=u"任务发布人", default=1)
    name = models.CharField(max_length=20, verbose_name=u"名称")
    urls = models.TextField(verbose_name=u"URL明细")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=u"投放时间")
    update_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = u"多URL列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_name.username+":"+self.task_id