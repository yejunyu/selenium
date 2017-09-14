# -*- coding: utf-8 -*-

import datetime
import hashlib
import time
import traceback

from django.http import HttpResponse
from django.shortcuts import render
from browser.models import ClickTask, TimeTask, TaskCount
from users.models import UserProfile
from .models import CPMWork, CPCWork
from django.contrib.auth.decorators import login_required

from tools import utils
# Create your views here.
@login_required(login_url='login')
def createCPM(request):
    return render(request, 'createCPM.html')


@login_required(login_url='login')
def CPM(request):
    try:
        # 获取数据
        task_area = request.POST.get('task_area')
        flow_demand = request.POST.get('flow_demand')
        referer = request.POST.get('referer')
        remaintime = request.POST.get('remaintime')
        url = request.POST.get('url')
        tfip = request.POST.get('tfip')
        pvbs = request.POST.get('pvbs')
        is_control = request.POST.get('is_control')
        task_time = request.POST.get('task_time')
        remark = request.POST.get('remark')
        user_id = request.POST.get('user_id')
        # 计算和处理
        md5 = hashlib.md5()
        md5.update((url + str(time.time())).encode('utf8'))
        url_md5 = md5.hexdigest()
        if tfip.isdigit():
            tfip = int(tfip)
        else:
            raise Exception(u"投放ip请输入数字")
        # click_task
        if task_time:
            task_time = datetime.datetime.strptime(task_time,'%Y-%m-%d')
            if task_time < datetime.datetime.now():
                raise Exception(u'任务日期小于当前时间,请检查!')
        else:
            task_time = datetime.date.today() + datetime.timedelta(days=1)
        click_task = {'url':url,'url_md5':url_md5,'task_time':task_time,'task_area':task_area,'pv':pvbs,'user_id':user_id}
        if int(flow_demand) == 0 or int(flow_demand) == 1:
            if int(flow_demand) == 1:
                if remaintime.isdigit():
                    click_task['remaintime'] = remaintime
                if referer:
                    click_task['referer'] = referer
            click_task['task_detail'] = 0
        else:
            if int(flow_demand) == 3:
                if remaintime:
                    click_task['remaintime'] = remaintime
                if referer:
                    click_task['referer'] = referer
            click_task['task_detail'] = 1
        click_task['remark'] = remark if remark else u'无'
        task_id = ClickTask.objects.create(**click_task).id
        # task_count
        task_count = {'url_md5':url_md5,'task_count':tfip,'task_id_id':task_id}
        TaskCount.objects.create(**task_count)
        # time_task
        time_task = {'url_md5':url_md5,'task_id_id':task_id}
        if int(is_control) == 0:
            count = int(tfip/24)
            for i in range(24):
                time_task['field_'+str(i)] = count
        elif int(is_control) == 1:
            for i in range(24):
                time_task['field_'+str(i)] = request.POST.get(str(i))
        TimeTask.objects.create(**time_task)
        # business_cpmwork
        cpmwork = {'user_name_id':user_id,'task_id_id':task_id,'url':url,'click_nums':tfip,'ip_nums':0,'pv_nums':0,'status':0,'is_control':is_control,'remark':remark,'task_time':task_time}
        CPMWork.objects.create(**cpmwork)
        # cpmwork['task_time'] = time.strftime('%Y-%m-%d %X',time.localtime())
        return render(request, 'CPMWork.html', {'cpmworks':[cpmwork]})
        # return HttpResponse(click_task)
    except Exception as e:
        utils.write_debug(utils.LINE(), 'business/views', traceback.print_exc())
        return HttpResponse(e)


@login_required(login_url='login')
def CPMTask(request):
    cpmworks = CPMWork.objects.filter(user_name_id=request.user.id)
    print (cpmworks)
    return render(request, 'CPMWork.html', {'cpmworks':cpmworks})


@login_required(login_url='login')
def createCPC(request):
    return render(request, 'createCPC.html')


@login_required(login_url='login')
def CPC(request):
    try:
        # 获取数据
        task_area = request.POST.get('task_area')
        flow_demand = request.POST.get('flow_demand')
        referer = request.POST.get('referer')
        remaintime = request.POST.get('remaintime')
        url = request.POST.get('url')
        tfip = request.POST.get('tfip')
        pvbs = request.POST.get('pvbs')
        is_control = request.POST.get('is_control')
        task_time = request.POST.get('task_time')
        remark = request.POST.get('remark')
        user_id = request.POST.get('user_id')
        sectime = request.POST.get('sectime')
        securl = request.POST.get('codeGist') or request.POST.get('codeElement')
        task_bili = request.POST.get('task_bili')
        pzff = request.POST.get('pzff')
        # 计算和处理
        md5 = hashlib.md5()
        md5.update((url + str(time.time())).encode('utf8'))
        url_md5 = md5.hexdigest()
        if tfip.isdigit():
            tfip = int(tfip)
        else:
            raise Exception(u"投放ip请输入数字")
        # click_task
        if task_time:
            task_time = datetime.datetime.strptime(task_time,'%Y-%m-%d')
            if task_time < datetime.datetime.now():
                raise Exception(u'任务日期小于当前时间,请检查!')
        else:
            task_time = datetime.date.today() + datetime.timedelta(days=1)
        click_task = {'url':url,'url_md5':url_md5,'task_time':task_time,'task_area':task_area,'pv':pvbs,'user_id':user_id,'referer':referer,'remaintime':remaintime,'sectime':sectime,'task_type':1}
        if int(flow_demand) == 0:
            pass
        elif int(flow_demand) == 1:
            pass
        elif int(flow_demand) == 2:
            pass
        else:
            pass
        if int(pzff) == 0:
            click_task['securl'] = securl
        elif int(pzff) == 1:
            pass
        else:
            pass
        click_task['remark'] = remark if remark else u'无'
        task_id = ClickTask.objects.create(**click_task).id
        # task_count
        task_count = {'url_md5':url_md5,'task_count':tfip,'task_id_id':task_id}
        TaskCount.objects.create(**task_count)
        # time_task
        time_task = {'url_md5':url_md5,'task_id_id':task_id}
        if int(is_control) == 0:
            count = int(tfip/24)
            for i in range(24):
                time_task['field_'+str(i)] = count
        elif int(is_control) == 1:
            for i in range(24):
                time_task['field_'+str(i)] = request.POST.get(str(i))
        TimeTask.objects.create(**time_task)
        # business_cpcwork
        cpcwork = {'user_name_id':user_id,'task_id_id':task_id,'url':url,'click_nums':tfip,'ip_nums':0,'hasclicked':0,'status':0,'is_control':is_control,'remark':remark,'task_time':task_time}
        CPCWork.objects.create(**cpcwork)
        # cpcwork['task_time'] = time.strftime('%Y-%m-%d %X',time.localtime())
        return render(request, 'CPCWork.html', {'cpcworks':[cpcwork]})
        # return HttpResponse(click_task)
    except Exception as e:
        utils.write_debug(utils.LINE(), 'business/views', traceback.print_exc())
        return HttpResponse(e)


@login_required(login_url='login')
def CPCTask(request):
    cpcworks = CPCWork.objects.filter(user_name_id=request.user.id)
    print (cpcworks)
    return render(request, 'CPCWork.html', {'cpcworks':cpcworks})
