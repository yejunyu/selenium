from __future__ import absolute_import
#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__ = 'Ye Jun yu'
# email: yyyejunyu@gmail.com
# date:{17-6-28}

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "adClick.settings")
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(BASE_DIR))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))
print (os.path)
print (sys.path)
import django
django.setup()
from celery import Celery
from django.conf import settings

app = Celery('yejunyu',backend='amqp', broker='amqp://admin:asdf123456asdf@localhost:5672//')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)