#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__ = 'Ye Jun yu'
# email: yyyejunyu@gmail.com
# date:{17-6-26}

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
from apps.browser import models
TaskCount = models.TaskCount.objects

def browser_click1(url,proxy):
    try:
        WIDTH = 1336
        HEIGHT = 750
        PIXEL_RATIO = 3.0
        UA = random.choice(userAgent.USERAGENT['google'] + userAgent.USERAGENT['ios'])
        mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
        options = webdriver.ChromeOptions()
        # proxy = int(proxy)
        # ip = utils.get_proxy(1,proxy)
        # utils.write_debug(utils.LINE(), 'browser', ip)
        # options.add_argument('--proxy-server=%s' % ip)
        options.add_argument("headless")
        options.add_argument("disable-gpu")
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        driver = webdriver.Chrome(chrome_options=options)
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.get(url)
        time.sleep(30 + random.random() * 30)
        # el = WebDriverWait(driver,60,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="bs-example-navbar-collapse-1"]/ul/li[3]/a')))
        # el.click()
        # time.sleep(random.random() * 5)
        driver.quit()
    except Exception:
        driver.quit()
        utils.write_debug(utils.LINE(), 'browser', traceback.print_exc())


def browser_click(url, count, proxy, md5):
    pool = multiprocessing.Pool(processes=50)
    for i in range(int(count)):
        pool.apply_async(browser_click1,args=(url,proxy))
        time.sleep(1)
    pool.close()
    pool.join()
    # pool = ThreadPoolExecutor(max_workers=10)
    # futures = []
    # for i in range(int(count)):
    #     futures.append(pool.submit(browser_click1, url, proxy))
    #     time.sleep(1)
    # print(wait(futures, timeout=60))
    if md5 != 0:
        result = TaskCount.get(url_md5=md5)
        result.finish_count += count
        result.save(update_fields=['finish_count'])


if __name__ == '__main__':
    url = sys.argv[1]
    count = sys.argv[2]
    browser_click(url, count, 0, 0)

