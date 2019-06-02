# -*- coding: utf-8 -*-
import json
from urllib.request import urlopen, quote
import requests,csv
#import pandas as pd #导入这些库后边都要用到
import time

def getlnglat(address, ak):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    #ak = '2FwFxZMZMGBU77lQnyuIHNNDutiDQSTe'     # 自己申请的ak
    #ak = 'cxm6o7jDpBvtlgi1H3hVmk439xt4ff3f'
    add = quote(address) #由于地址变量为中文，为防止乱码，先用quote进行编码
    uri = url + '?' + 'address=' + add  + '&output=' + output + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode() #将其他编码的字符串解码成unicode
    temp = json.loads(res) #对json数据进行解析
    return temp

file = open(r'D:\\Scrapy\keti\keti\point.json','w') #建立json数据文件
with open(r'D:\\Scrapy\keti\keti\keti.csv', 'r', encoding='utf-8') as csvfile: #打开csv
    reader = csv.reader(csvfile)
    ak1 = '2FwFxZMZMGBU77lQnyuIHNNDutiDQSTe'
    ak2 = 'cxm6o7jDpBvtlgi1H3hVmk439xt4ff3f'
    num = 1
    for line in reader: #读取csv里的数据
        # 忽略第一行
        if reader.line_num == 1: #由于第一行为变量名称，故忽略掉
            continue             # line是个list，取得所有需要的值

        b = line[2].strip()     #将第一列address读取出来并清除不需要字符
        c= line[3].strip()      #将第二列money读取出来并清除不需要字符

        lng = getlnglat("西安市" + b, ak2)['result']['location']['lng'] #采用构造的函数来获取经度
        lat = getlnglat("西安市" + b, ak2)['result']['location']['lat'] #获取纬度
        str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) + ',"count":' + str(c) +'},'

        print(num, str_temp) #也可以通过打印出来，把数据copy到百度热力地图api的相应位置上
        num += 1
        file.write(str_temp) #写入文档
        if num%100 == 0:
            time.sleep(10)
file.close() #保存
