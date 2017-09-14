#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'Ye Jun yu'
# email: yyyejunyu@gmail.com
# date:{17-7-17}

import xadmin
from xadmin import views
from .models import EmailVerifyRecord, EmailBox


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "广告点击后台管理系统"
    site_footer = u"聚诚仁和"
    menu_style = "accordion"


# class UserProfileAdmin(object):
#     list_display = ['id', 'username', 'mobile', 'email','last_login']
#     search_fields = ['id', 'username', 'mobile', 'email']
#     list_filter = ['id', 'username', 'mobile', 'email','last_login']


class EmailVerifyRecordAdmin(object):
    list_display = ['user_name', 'code', 'email', 'send_type', 'send_time']
    search_fields = ['user_name', 'code', 'email', 'send_type']
    list_filter = ['user_name__username', 'code', 'email', 'send_type', 'send_time']


class EmailBoxAdmin(object):
    list_display = ['user_name', 'title', 'content', 'create_at']
    search_fields = ['user_name', 'title', 'content']
    list_filter = ['user_name__username', 'title', 'content', 'create_at']


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(EmailBox, EmailBoxAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
