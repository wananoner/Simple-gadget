# -*- coding : utf-8 -*-
import requests
import json
from time import time

def open_url(url, **params):
    req = requests.get(url, **params)
    js = req.json(encoding='utf-8')

    return js

def jixi(js_1):
    name = js_1['data']['result']
    for i in name:
        print(i['name'])
        for a in i['capital']:
            print(a['percent'])
            print(a['amomon'])

def main():
    keywords = input("请输入需要查询公司的名称： ")
    start = time()
    url = 'http://www.tianyancha.com/search/' + keywords + '.json?'
    url_1 = 'http://www.tianyancha.com/expanse/holder.json'
    js = open_url(url)
    company_id = js['data'][0]['id']
    param = {
    'id' : company_id,
    'ps' : 20,
    'pn' : 1
    }
    js_1 = open_url(url_1, params=param)
    jixi(js_1)
    end = time()
    print(end - start)

if __name__ == "__main__":
    main()
