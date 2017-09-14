#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__ = 'Ye Jun yu'
# email: yyyejunyu@gmail.com
# date:{17-6-26}

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait
import multiprocessing
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), './../../'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "adClick.settings")
import django
django.setup()
import random
import time
from selenium import webdriver
from tools import userAgent, utils
import traceback
from bs4 import BeautifulSoup
# from apps.browser import models
# TaskCount = models.TaskCount.objects


def browser_click1(url,proxy,referer,remaintime,task_detail,pv,width,height,is_random,sectime,securl,element,task_type):
    try:
        WIDTH = width
        HEIGHT = height
        PIXEL_RATIO = 3.0
        if task_detail == 0:
            UA = random.choice(userAgent.USERAGENT['pc'])
        elif task_detail == 1:
            UA = random.choice(userAgent.USERAGENT['google'] + userAgent.USERAGENT['ios'])
        elif task_detail == 2:
            UA = random.choice(userAgent.USERAGENT['ios'])
        else:
            UA = random.choice(userAgent.USERAGENT['google'])
        mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
        if referer:
            referer = random.choice(referer.split(';'))
            pass
        options = webdriver.ChromeOptions()
        if int(proxy) == 9999:
            pass
        else:
            proxy = int(proxy)
            ip = utils.get_proxy(proxy)
            utils.write_debug(utils.LINE(), 'browser', ip)
            options.add_argument('--proxy-server=%s' % ip)
        options.add_argument("headless")
        options.add_argument("disable-gpu")
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        driver = webdriver.Chrome(chrome_options=options)
        driver.set_page_load_timeout(60)
        driver.implicitly_wait(60)
        driver.get(url)
        for i in range(pv-1):
            js = 'window.open("{}");'.format(url)
            driver.execute_script(js)
        time.sleep(random.uniform(remaintime-3,remaintime+3))

        '''
        CPC
        '''
        if task_type == 1:
            if is_random == 1:
                urls = BeautifulSoup(driver.page_source,'lxml').find_all('a')
                url = random.choice(urls).get('href')
                driver.get(url)
                time.sleep(sectime)
            else:
                if securl:
                    # <a class="swf-top" href="http://tv.sohu.com/s2015/dsjwxfs" target="_blank"></a>
                    urls = securl.split(';')
                    url = random.choice(urls)
                    print(url)
                    driver.get(url)
                    time.sleep(sectime)
            # soup.findAll('a',{'class':'lb'})
            # Out[14]: [<a class="lb" href="http://www.baidu.com/bdorz/login.gif?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2f%3fbdorz_come%3d1" name="tj_login">ç»å½</a>]
                elif element:
                    element_key = element.split(':')[0]
                    element_value = element.split(':')[1]
                    urls = BeautifulSoup(driver.page_source, 'lxml').findAll('a',{element_key:element_value})
                    url = random.choice(urls)
                    driver.get(url)
                    time.sleep(sectime)
        # el = WebDriverWait(driver,60,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="bs-example-navbar-collapse-1"]/ul/li[3]/a')))
        # el.click()
        # time.sleep(random.random() * 5)
        print(driver.title)
        driver.get('about:blank')
        driver.close()
        driver.quit()
    except Exception as e:
        print(e)
        driver.close()
        driver.quit()
        utils.write_debug(utils.LINE(), 'browser', traceback.print_exc())


def browser_click(params):
    url = 'url' in params and params['url'] or None
    count = 'count' in params and params['count'] or 1
    proxy = 'task_area' in params and params['task_area'] or 9999
    referer = 'referer' in params and params['referer'] or None
    remaintime = 'remaintime' in params and params['remaintime'] or 3
    task_detail = 'task_detail' in params and params['task_detail'] or 0
    pv = 'pv' in params and params['pv'] or 1
    width = 'width' in params and params['width'] or 1366
    height = 'height' in params and params['height'] or 768
    is_random = 'is_random' in params and params['is_random'] or 0
    sectime = 'sectime' in params and params['sectime'] or 1
    securl = 'securl' in params and params['securl'] or None
    element = 'element' in params and params['element'] or None
    task_type = 'task_type' in params and params['task_type'] or None
    '''
    # {'url': 'http://', 'pv': 1, 'task_detail': 0, 'count': 100, 'referer': None, 'user': 1, 'task_status': 0,
    # 'task_area': '9999', 'task_time': '2017-08-10', 'remark': '无', 'update_at': '2017-08-09T10:22:39', 'sectime': None, 
    # 'securl': None, 'task_type': 0, 'task_bili': 0, 'request': 1, 'remaintime': None, 'bk1': None, 'reate_at': '2017-08-09T09:59:40'}

    '''

    print (params)
    try:
        pool = multiprocessing.Pool(processes=10)
        for i in range(int(count)):
            pool.apply_async(browser_click1,args=(url,proxy,referer,remaintime,task_detail,pv,width,height,is_random,sectime,securl,element,task_type))
            time.sleep(1)
        pool.close()
        pool.join()
    except Exception as e:
        print (e)

    # try:
    #     pool = ProcessPoolExecutor(max_workers=10)
    #     futures = []
    #     for i in range(int(count)):
    #         futures.append(pool.submit(browser_click1,url,proxy,referer,remaintime,task_detail,pv,width,height,is_random,sectime,securl,element,task_type))
    #         time.sleep(1)
    #     print(wait(futures, timeout=60))
    # except Exception as e:
    #     print (e)


if __name__ == '__main__':
    params = {
        'url':sys.argv[1],
        'count':sys.argv[2],
        'securl':sys.argv[3],
        'task_type':1,
    }
    browser_click(params)

