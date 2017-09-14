#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__ = 'Ye Jun yu'
# email: yyyejunyu@gmail.com
# date:{17-6-27}

import os
import sys

import requests

sys.path.append(os.path.join(os.path.dirname(__file__), './../../'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "adClick.settings")
import django
django.setup()
import time
import random
from concurrent.futures import ThreadPoolExecutor, wait
from browser import models
TaskCount = models.TaskCount.objects
from tools import utils, userAgent
import traceback


def click1(url,proxy):
    try:
        ip = utils.get_proxy(1,proxy)
        utils.write_debug(utils.LINE(), 'request', ip)
        proxies = {"http": "http://" + ip, "https": "https://" + ip}
        UA = random.choice(userAgent.USERAGENT['pc'])
        headers = {"User-Agent": UA}
        requests.adapters.DEFAULT_RETRIES = 5
        session = requests.session()
        session.keep_alive = False
        session.get(url, proxies=proxies, headers=headers)
        time.sleep(30+random.random()*30)
    except Exception:
        utils.write_debug(utils.LINE(), 'request', traceback.print_exc())


def click(url, count, proxy,md5):
    pool = ThreadPoolExecutor(max_workers=10)
    futures = []
    for i in range(int(count)):
        futures.append(pool.submit(click1, url,proxy))
        time.sleep(1)
    print(wait(futures, timeout=60))
    result = TaskCount.get(url_md5=md5)
    result.finish_count += count
    result.save(update_fields=['finish_count'])


if __name__ == '__main__':
    url = sys.argv[1]
    count = sys.argv[2]
    click(url, count, 0)