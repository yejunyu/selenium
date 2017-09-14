import datetime
import hashlib
import time

from django.http import HttpResponse
from django.shortcuts import render
from .models import ClickTask, TaskCount, TimeTask

ClickTask = ClickTask.objects
TimeTask = TimeTask.objects
TaskCount = TaskCount.objects
from tools import utils
import traceback

# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def other(request):
    return render(request,'other.html')

def createCPM(request):
    return render(request, 'createCPM.html')

def CPM(request):
    print(request.POST)
    return HttpResponse(request.POST)

def CPC(request):
    print(request.POST)
    print ('1')
    print (request.POST.get('task_date'))
    return HttpResponse(request.POST)

def dosql(request):
    try:
        url = request.GET.get('url')
        task_detail = request.GET.get('task_detail')
        task_time = request.GET.get('task_time')
        if task_time:
            task_time = datetime.datetime.strptime(task_time,'%Y-%mm-%d')
            if task_time < datetime.datetime.now():
                return HttpResponse('任务发布失败,请检查任务开始的时间!')
        else:
            task_time = datetime.date.today() + datetime.timedelta(days=1)
        md5 = hashlib.md5()
        md5.update((url+str(time.time())).encode('utf8'))
        MD5 = md5.hexdigest()
        app_clicktask = {'url': url, 'url_md5': MD5,'task_detail': task_detail,'task_time':task_time}
        ClickTask.create(**app_clicktask)
        ClickTask.objects.filter(id)
        if int(task_detail) == 0:
            task_count = request.GET.get('task_count')
            app_taskcount = {'url_md5': MD5,'task_count': task_count}
            TaskCount.create(**app_taskcount)
        else:
            app_timetask = {'url_md5': MD5}
            task_count = 0
            for i in range(24):
                app_timetask['field_'+str(i)] = request.GET.get(str(i))
                task_count += int(request.GET.get(str(i)))
            TimeTask.create(**app_timetask)
            app_taskcount = {'url_md5': MD5, 'task_count': task_count}
            TaskCount.create(**app_taskcount)
        return HttpResponse('任务发布成功,您的任务编号为: '+MD5)
    except Exception as e:
        utils.write_debug(utils.LINE(), 'dosql', traceback.print_exc())
        return HttpResponse('任务发布失败\n'+str(e))
