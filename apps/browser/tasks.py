#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__ = 'Ye Jun yu'
# email: yyyejunyu@gmail.com
# date:{17-6-28}

from celery.schedules import crontab

from adClick.myCelery import app

app.conf.timezone = 'Asia/Shanghai'
from apps.browser import models
ClickTask = models.ClickTask.objects
TimeTask = models.TimeTask.objects
TaskCount = models.TaskCount.objects
import time
import datetime
from tools import utils
import multiprocessing
from django.core import serializers
import json
from apps.browser import browser
from apps.browser import request
import traceback


@app.on_after_configure.connect
def periodic_task(sender, **kwargs):
    # 每小时任务(取 time_task,控量)
    sender.add_periodic_task(
        crontab(minute=0),
        hour_task.s(),
    )
    # 每分钟检查任务完成数
    sender.add_periodic_task(
        crontab(),
        check_task.s(),
    )
    # # 不控量的,每日0点开始
    # sender.add_periodic_task(
    #     crontab(hour=0,minute=0),
    #     day_task.s(),
    # )

# celery -A browser.tasks worker -l info -B
@app.task
def hour_task():
    # 控量,每小时查找任务
    print ('start')
    now = datetime.datetime.now()
    hour = 'field_' + str(now.hour)
    # 进程队列
    ts = []
    # 查找status不为2,且时间已到的任务
    try:
        query_results = ClickTask.filter(task_status__in=[0, 1], task_time=datetime.date.today())
        for query_result in query_results:
            # url = query_result.url
            md5 = query_result.url_md5
            # proxy = query_result.task_area
            time_task_obj = TimeTask.get(url_md5=md5)
            # querySet序列化
            time_task_dic = json.loads(serializers.serialize('json', [time_task_obj]))[0]
            count = time_task_dic['fields'][hour]
            params = json.loads(serializers.serialize('json', [query_result]))[0]['fields']
            params['count'] = count
            # celery中起子进程会报错
            # AssertionError: daemonic processes are not allowed to have children
            process = multiprocessing.current_process()
            # 进程启动前设为非守护进程启动
            process.daemon = False
            p = multiprocessing.Process(target=browser.browser_click, args=(params,)) \
                if int(query_result.request) == 1 else multiprocessing.Process(target=request.click,
                                                                               args=(params,))
            p.start()
            ts.append(p)
            # 启动后再设为true
            process.daemon = True
            utils.write_debug(utils.LINE(), 'tasks', 'start:' + md5+' time: '+time.strftime('%X')+'\ncount:'+str(count))
        # status置位
        query_results.update(task_status=1)
        for t in ts:
            t.join()
    except Exception:
        utils.write_debug(utils.LINE(), 'tasks', traceback.print_exc())


@app.task
def check_task():
    try:
        results = TaskCount.filter(task_status=0)
        for result in results:
            if result.finish_count >= result.task_count:
                result.task_status = 1
                md5 = result.url_md5
                result.save(update_fields=['task_status'])
                q = ClickTask.get(url_md5=md5)
                q.task_status = 2
                q.save(update_fields=['task_status'])
    except Exception:
        utils.write_debug(utils.LINE(), 'tasks', traceback.print_exc())


# @app.task
# def day_task():
#     # 不控量
#     today = datetime.date.today()
#     # 进程队列
#     ts = []
#     # 查找status不为2,且时间已到的任务
#     try:
#         query_results = ClickTask.filter(task_status=0, task_detail=0, task_time=today)
#         for query_result in query_results:
#             url = query_result.url
#             md5 = query_result.url_md5
#             proxy = query_result.task_area
#             task_count_obj = TaskCount.get(url_md5=md5)
#             # querySet序列化
#             time_task_dic = json.loads(serializers.serialize('json', [task_count_obj]))[0]
#             count = time_task_dic['fields']['task_count']
#             # celery中起子进程会报错
#             # AssertionError: daemonic processes are not allowed to have children
#             process = multiprocessing.current_process()
#             # 进程启动前设为非守护进程启动
#             process.daemon = False
#             p = multiprocessing.Process(target=browser.browser_click, args=(url, count, proxy, md5)) \
#                 if int(query_result.request) == 1 else multiprocessing.Process(target=request.click,
#                                                                                args=(url, count, proxy,md5))
#             p.start()
#             ts.append(p)
#             # 启动后再设为true
#             process.daemon = True
#             utils.write_debug(utils.LINE(), 'tasks',
#                               'start:' + md5 + ' time: ' + time.strftime('%X') + '\ncount:' + str(count))
#         # status置位
#         query_results.update(task_status=1)
#         for t in ts:
#             t.join()
#     except Exception:
#         utils.write_debug(utils.LINE(), 'tasks', traceback.print_exc())