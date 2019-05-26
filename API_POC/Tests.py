#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-06-09 14:22
# jiaoben.py

from paras import ZHCS
from config import API_ALL
from Wrappers import tool
import requests
# 脚本类，组合工具参数进行请求
gj = tool()
def jball():
    apikeys = API_ALL.keys()
    print(apikeys)
    for key in apikeys:
        apiname = key
        url = API_ALL[key]['url']
        number = API_ALL[key]['number']
        method = API_ALL[key]['method']
        paras = gj.listalls(API_ALL[key]['para'], ZHCS)
        if method == 'post':
            print("======="+" api name:"+apiname+"=======")
            print("Method: Post")
            for cs in paras:
                mp = requests.post(url=url, data=cs)
                print ('haha')
                print (mp)
                print (cs)
                res_code = str(mp.status_code)
                res_time = str(mp.elapsed.microseconds)
                print("api number ："+number+"  response code："+res_code+"  response time:"+res_time)
        if method == 'get':
            print("======="+" api :"+apiname+"=======")
            print("MEthod: get")
            for cs in paras:
                mp = requests.get(url=url, data=cs)
                res_code = str(mp.status_code)
                res_time = str(mp.elapsed.microseconds)
                print (cs)
                print("api ："+number+"  respomse code："+res_code+"  response time:"+res_time)
jball()