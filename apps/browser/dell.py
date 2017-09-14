#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__ = 'Ye Jun yu'
# email: yyyejunyu@gmail.com
# date:{17-6-27}

import requests
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), './../../'))
import time
import random
from concurrent.futures import ThreadPoolExecutor, wait
from tools import utils, userAgent
import traceback
from bs4 import BeautifulSoup

def click1(url):
    try:
        ip = utils.get_proxy(1)
        utils.write_debug(utils.LINE(), 'request', ip)
        proxies = {"http": "http://" + ip, "https": "https://" + ip}
        UA = random.choice(userAgent.USERAGENT['pc'])
        headers = {"User-Agent": UA,"Referer":"http://www.ebrun.com/retail/b2c/"}
        requests.adapters.DEFAULT_RETRIES = 5
        session = requests.session()
        session.keep_alive = False
        r = session.get(url, proxies=proxies, headers=headers)
        time.sleep(random.random() * 3)
        soup = BeautifulSoup(r.text,'lxml')
        links = soup.find_all('a',class_='buyEm')
        link = random.choice(links)
        url = link.get('href')
        print (url)
        session.get(url, proxies=proxies, headers=headers)
        time.sleep(random.random()*30)
    except Exception:
        utils.write_debug(utils.LINE(), 'request', traceback.print_exc())


def click(url, count):
    pool = ThreadPoolExecutor(max_workers=10)
    futures = []
    for i in range(int(count)):
        futures.append(pool.submit(click1, (url)))
        time.sleep(1)
    print(wait(futures, timeout=60))



if __name__ == '__main__':
    url = 'http://adfarm.mediaplex.com/ad/ck/10592-210885-45941-45'
    count = sys.argv[1]
    click(url, count)