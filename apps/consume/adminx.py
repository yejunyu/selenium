#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__ = 'Ye Jun yu'
# email: yyyejunyu@gmail.com
# date:{17-7-20}

from extra_apps import xadmin
from .models import MyCharge, MyConsume

class MyChargeAdmin(object):
    list_display = ['user_name', 'id', 'create_at', 'money', 'remark']
    search_fields = ['user_name', 'id', 'money', 'remark']
    list_filter = ['user_name__username', 'id', 'create_at', 'money', 'remark']


class MyConsumeAdmin(object):
    list_display = ['user_name', 'id', 'task_id', 'type', 'reason', 'money', 'create_at']
    search_fields = ['user_name', 'id', 'task_id', 'type', 'reason', 'money']
    list_filter = ['user_name__username', 'id', 'task_id', 'type', 'reason', 'money', 'create_at']


xadmin.site.register(MyCharge, MyChargeAdmin)
xadmin.site.register(MyConsume, MyConsumeAdmin)