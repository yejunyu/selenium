#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__ = 'Ye Jun yu'
# email: yyyejunyu@gmail.com
# date:{17-7-20}

from extra_apps import xadmin
from .models import CPMWork, CPCWork, CPMHistory, CPCHistory, RankWork, Urls

class CPMWorkAdmin(object):
    list_display = ['user_name', 'task_id', 'url', 'click_nums', 'ip_nums', 'pv_nums', 'is_control', 'status', 'task_time', 'remark']
    search_fields = ['user_name', 'task_id__id', 'url', 'click_nums', 'ip_nums', 'pv_nums', 'is_control', 'status', 'remark']
    list_filter = ['user_name__username', 'task_id__id', 'url', 'click_nums', 'ip_nums', 'pv_nums', 'is_control', 'status', 'task_time', 'remark']


class CPCWorkAdmin(object):
    list_display = ['user_name', 'task_id', 'url', 'click_nums', 'hasclicked', 'ip_nums', 'is_control', 'status', 'task_time', 'remark']
    search_fields = ['user_name', 'task_id', 'url', 'click_nums', 'hasclicked', 'ip_nums', 'is_control', 'status', 'remark']
    list_filter = ['user_name__username', 'task_id', 'url', 'click_nums', 'hasclicked', 'ip_nums', 'is_control', 'status', 'task_time', 'remark']


class RankWorkAdmin(object):
    list_display = ['user_name', 'task_id', 'url', 'click_nums', 'hasclicked', 'ip_nums', 'is_control',
                    'status', 'task_time']
    search_fields = ['user_name', 'task_id', 'url', 'click_nums', 'hasclicked', 'ip_nums', 'is_control',
                     'status']
    list_filter = ['user_name__username', 'task_id', 'url', 'click_nums', 'hasclicked', 'ip_nums', 'is_control',
                   'status', 'task_time']


class CPMHistoryAdmin(object):
    list_display = ['user_name', 'task_id', 'url', 'click_nums', 'ip_nums', 'pv_nums',
                    'history']
    search_fields = ['user_name', 'task_id', 'url', 'click_nums', 'ip_nums', 'pv_nums',
                    'history']
    list_filter = ['user_name__username', 'task_id', 'url', 'click_nums', 'ip_nums', 'pv_nums',
                    'history']


class CPCHistoryAdmin(object):
    list_display = ['user_name', 'task_id', 'url', 'click_nums', 'ip_nums', 'pv_nums',
                    'history']
    search_fields = ['user_name', 'task_id', 'url', 'click_nums', 'ip_nums', 'pv_nums',
                     'history']
    list_filter = ['user_name__username', 'task_id', 'url', 'click_nums', 'ip_nums', 'pv_nums',
                   'history']


class UrlsAdmin(object):
    list_display = ['user_name', 'id', 'name', 'urls']
    search_fields = ['user_name', 'id', 'name', 'urls']
    list_filter = ['user_name__username', 'id', 'name', 'urls']


xadmin.site.register(CPMWork, CPMWorkAdmin)
xadmin.site.register(CPCWork, CPCWorkAdmin)
xadmin.site.register(RankWork, RankWorkAdmin)
xadmin.site.register(CPMHistory, CPMHistoryAdmin)
xadmin.site.register(CPCHistory, CPCHistoryAdmin)
xadmin.site.register(Urls, UrlsAdmin)