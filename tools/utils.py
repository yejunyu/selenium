#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'Ye Jun yu'
# email: yyyejunyu@gmail.com
# date:{DATE}


import os
import sys
import subprocess
import requests
import traceback
import time
import socket, struct

# 调用系统命令
def cust_popen(cmd, close_fds=True):
    proc = subprocess.Popen('%s' % cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=close_fds)
    retcode = proc.wait()
    return retcode, proc


# 获取代理 ip:port
def get_proxy1(count=100,proxy=0):
    url = 'http://s.zdaye.com/?api=201707051117373074&count=5&fitter=1&px=1'
    r = requests.get(url).text
    if r.find('bad') == -1:
        return r.split('\r\n')
    else:
        time.sleep(2)
        return get_proxy()

def get_proxy(count=100,proxy=0):
    if proxy==0:
        url = 'http://api.ip.data5u.com/api/get.shtml?order=57affdc6f7fd6219409a59df5d9c3a16&num=1&area=%E4%B8%AD%E5%9B%BD&carrier=0&protocol=0&an1=1&an2=2&an3=3&sp1=1&sp2=2&sp3=3&sort=1&system=1&distinct=0&rettype=1&seprator=%0D%0A'
        # url = 'http://api.ip.data5u.com/dynamic/get.html?order=57affdc6f7fd6219409a59df5d9c3a16&sep=0'
    if proxy==1:
        url = 'http://api.ip.data5u.com/api/get.shtml?order=57affdc6f7fd6219409a59df5d9c3a16&num=1&area=%E5%B9%BF%E5%B7%9E%E5%B8%82&carrier=0&protocol=0&an1=1&an2=2&an3=3&sp1=1&sp2=2&sp3=3&sort=1&system=1&distinct=0&rettype=1&seprator=%0D%0A'
    r = requests.get(url)
    return r.text.strip()


# 日志打印
logpath = os.path.join(os.getcwd(),os.path.dirname(__file__))
if logpath not in sys.path:
    sys.path.append(logpath)
debugfile = os.path.join(logpath,'../log/log.log')
def LINE ():
    return traceback.extract_stack()[-2][1]
def write_debug (line,module,errdata = None):
    if os.path.isfile(debugfile) == False:
        os.mknod(debugfile)
    nowtime = time.strftime("%Y-%m-%d %X")
    if errdata is None:
        err_data = '%s %s [line:%s]: ' %(nowtime,module,line)
        f = open(debugfile,'a')
        f.write(err_data)
        traceback.print_exc(file = f)
        f.flush()
        f.close()
    else:
        err_data = '%s %s [line:%s]: %s\n' %(nowtime,module,line,errdata)
        f = open(debugfile,'a')
        f.write(err_data)
        f.flush()
        f.close()


# ip整数互转 只限ipv4
def ip2int(ip):
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!L", packedIP)[0]
def int2ip(num):
    return socket.inet_ntoa(struct.pack('!L', int(num)))
