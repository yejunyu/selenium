# -*- coding: utf-8 -*-

import datetime

from django.db import models
from users.models import UserProfile


class ClickTask(models.Model):
    url = models.CharField(max_length=500)
    url_md5 = models.CharField(db_column='url_MD5', max_length=32, unique=True)  # Field name made lowercase.
    task_type = models.PositiveSmallIntegerField(default=0)
    task_detail = models.PositiveSmallIntegerField(default=0)
    task_status = models.PositiveSmallIntegerField(default=0)
    task_bili = models.PositiveSmallIntegerField(default=0)
    task_time = models.DateField(default=datetime.date.today)
    remaintime = models.PositiveSmallIntegerField(null=True, blank=True)
    pv = models.PositiveSmallIntegerField(choices=((1,'1'),(2,'2'),(3,'3')), default=1)
    # 以逗号分隔的数字,代表代理的地区
    task_area = models.CharField(max_length=255, validators=['validate_comma_separated_integer_list'], default=0)
    request = models.PositiveSmallIntegerField(default=1)
    referer = models.CharField(max_length=500, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    remark = models.TextField(blank=True, null=True)
    user = models.ForeignKey(UserProfile, default=1, verbose_name=u"任务发布人")
    securl = models.CharField(max_length=255,null=True,blank=True)
    sectime = models.PositiveSmallIntegerField(null=True, blank=True)
    bk1 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.url_md5

    class Meta:
        db_table = "click_task"


# class IpPool(models.Model):
#     ip = models.PositiveIntegerField()
#     port = models.PositiveIntegerField(blank=True, null=True)
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#     bk1 = models.CharField(max_length=255, blank=True, null=True)


class TaskCount(models.Model):
    task_id = models.ForeignKey(ClickTask, verbose_name=u"任务ID")
    url_md5 = models.CharField(db_column='url_MD5', max_length=32, unique=True)  # Field name made lowercase.
    finish_count = models.PositiveIntegerField(default=0)
    task_count = models.PositiveIntegerField(default=0)
    task_status = models.PositiveSmallIntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    bk1 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "task_count"


class TimeTask(models.Model):
    task_id = models.ForeignKey(ClickTask, verbose_name=u"任务ID")
    url_md5 = models.CharField(db_column='url_MD5', max_length=32, unique=True)  # Field name made lowercase.
    field_0 = models.PositiveIntegerField(db_column='_0', default=0)  # Field renamed because it started with '_'.
    field_1 = models.PositiveIntegerField(db_column='_1', default=0)  # Field renamed because it started with '_'.
    field_2 = models.PositiveIntegerField(db_column='_2', default=0)  # Field renamed because it started with '_'.
    field_3 = models.PositiveIntegerField(db_column='_3', default=0)  # Field renamed because it started with '_'.
    field_4 = models.PositiveIntegerField(db_column='_4', default=0)  # Field renamed because it started with '_'.
    field_5 = models.PositiveIntegerField(db_column='_5', default=0)  # Field renamed because it started with '_'.
    field_6 = models.PositiveIntegerField(db_column='_6', default=0)  # Field renamed because it started with '_'.
    field_7 = models.PositiveIntegerField(db_column='_7', default=0)  # Field renamed because it started with '_'.
    field_8 = models.PositiveIntegerField(db_column='_8', default=0)  # Field renamed because it started with '_'.
    field_9 = models.PositiveIntegerField(db_column='_9', default=0)  # Field renamed because it started with '_'.
    field_10 = models.PositiveIntegerField(db_column='_10', default=0)  # Field renamed because it started with '_'.
    field_11 = models.PositiveIntegerField(db_column='_11', default=0)  # Field renamed because it started with '_'.
    field_12 = models.PositiveIntegerField(db_column='_12', default=0)  # Field renamed because it started with '_'.
    field_13 = models.PositiveIntegerField(db_column='_13', default=0)  # Field renamed because it started with '_'.
    field_14 = models.PositiveIntegerField(db_column='_14', default=0)  # Field renamed because it started with '_'.
    field_15 = models.PositiveIntegerField(db_column='_15', default=0)  # Field renamed because it started with '_'.
    field_16 = models.PositiveIntegerField(db_column='_16', default=0)  # Field renamed because it started with '_'.
    field_17 = models.PositiveIntegerField(db_column='_17', default=0)  # Field renamed because it started with '_'.
    field_18 = models.PositiveIntegerField(db_column='_18', default=0)  # Field renamed because it started with '_'.
    field_19 = models.PositiveIntegerField(db_column='_19', default=0)  # Field renamed because it started with '_'.
    field_20 = models.PositiveIntegerField(db_column='_20', default=0)  # Field renamed because it started with '_'.
    field_21 = models.PositiveIntegerField(db_column='_21', default=0)  # Field renamed because it started with '_'.
    field_22 = models.PositiveIntegerField(db_column='_22', default=0)  # Field renamed because it started with '_'.
    field_23 = models.PositiveIntegerField(db_column='_23', default=0)  # Field renamed because it started with '_'.
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    bk1 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "time_task"