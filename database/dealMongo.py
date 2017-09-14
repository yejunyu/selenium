#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Ye Junyu'

import time
import traceback
import requests
import pymongo
import datetime
from tools import utils

DB = 'ad_click'
IP = '114.215.103.154'
PORT = 27018
USER = 'root'
PASSWD = 'asdf123456asdf'

def get_db(db=DB):
    try:
        # 建立连接
        client = pymongo.MongoClient(IP,PORT)
        db_auth = client.admin
        db_auth.authenticate(USER, PASSWD)
        # admin 数据库有帐号，连接-认证-切换库
        db = client[db]

        client['ad_click']['ip_pool'].create_index([("create_at", pymongo.ASCENDING)], expireAfterSeconds=30)
        return db
    except:
        utils.write_debug(utils.LINE(), "dealIp", traceback.print_exc())


def insert(datas, collection='ip_pool', db=DB):
    try:
        db = get_db(db)
        # for data in datas:
        #     data['create_at'] = time.strftime('%Y-%m-%d %H:%M:%S')
        result = db[collection].insert(datas)
        return result.inserted_ids
    except:
        utils.write_debug(utils.LINE(), "dealIp", traceback.print_exc())


def delete(collection, db=DB):
    pass


def update(data, condition, collection='ip_pool', db=DB):
    try:
        db = get_db(db)
        # "$currentDate": {"lastModified": True}
        data['update_at'] = time.strftime('%Y-%m-%d %H:%M:%S')
        db[collection].update_many(
            condition,
            {
                "$set": data,
            }
        )
    except:
        utils.write_debug(utils.LINE(), "dealIp", traceback.print_exc())



def select(condition={}, collection='ip_pool', db=DB):
    try:
        db = get_db(db)
        results = db[collection].find(condition)
        return list(results)
    except:
        utils.write_debug(utils.LINE(), "dealIp", traceback.print_exc())


def select_one(condition={}, collection='ip_pool', db=DB):
    try:
        db = get_db(db)
        results = db[collection].find_one(condition)
        return results
    except:
        utils.write_debug(utils.LINE(), "dealIp", traceback.print_exc())


def dealIp():
    m = 0
    try:
        datas = {}
        ips = utils.get_proxy(10)
        n = len(ips.split('\r\n'))
        for data in ips.split('\r\n'):
            datas['_id'] = data
            if select_one({'_id':data}, 'ip_pool'):
                pass
            else:
                insert([datas], 'ip_pool')
                m += 1
            datas = {}
        utils.write_debug(utils.LINE(), "dealIp", 'total ip num is {}'.format(n))
        utils.write_debug(utils.LINE(), "dealIp", 'success ip num is {}'.format(m))
    except:
        utils.write_debug(utils.LINE(), "dealIp", traceback.print_exc())

def dealIP():
    url = 'http://s.zdaye.com/?api=201707051117373074&count=5&fitter=1&px=1'
    r = requests.get(url).text
    datas = []
    if r.find('bad') == -1:
        ips = r.split('\r\n')
        for ip in ips:
            data = {"ip":ip,"create_at":datetime.datetime.utcnow()}
            datas.append(data)
        insert(datas)
        return r.split('\r\n')
