# # -*-coding: utf-8 -*-
# import requests
# import json
# from bs4 import BeautifulSoup
# from time import time
#
# def submit(url, content):
#     params = {
#         'type': 'AUTO',
#         'i': content,
#         'doctype': 'json',
#         'xmlVersion':  '1.8',
#         'keyfrom': 'fanyi.web',
#         'ue': 'UTF-8',
#         'action': 'FY_BY_ENTER',
#         'typoResult': 'true'
#         }
#     headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
#
#     html = requests.post(url, data=params, headers=headers)
#     html.encoding = 'utf-8'
#     soup = BeautifulSoup(html.text, 'html.parser').decode('utf-8')
#     return soup
#
# def input_results(soup):
#     try:
#         target = json.loads(soup)
#     except:
#         print("该词无法识别，请重新输入其他词汇")
#     else:
#         if "smartResult" in target:
#             if len(target['smartResult']['entries']) > 3:
#                 print("翻译结果：%s" % (''.join(target['translateResult'][0][0]['tgt'])),
#                       '\n\t',
#                       (''.join(target['smartResult']['entries'][1])),
#                       '\n\t',
#                       (''.join(target['smartResult']['entries'][2])),
#                       '\n\t',
#                       (''.join(target['smartResult']['entries'][3])))
#             elif len(target['smartResult']['entries']) > 2:
#                 print("翻译结果：%s" % (''.join(target['translateResult'][0][0]['tgt'])),
#                       '\n\t',
#                       (''.join(target['smartResult']['entries'][1])),
#                       '\n\t',
#                       (''.join(target['smartResult']['entries'][2])))
#             elif len(target['smartResult']['entries']) > 1:
#                 print("翻译结果：%s" % (''.join(target['translateResult'][0][0]['tgt'])),
#                       '\n\t',
#                       (''.join(target['smartResult']['entries'][1])))
#             else:
#                 print("请再试一次")
#         else:
#             print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))
#
# def main():
#     url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rul'
#     while True:
#         content = input("请输入需要翻译的内容： ")
#         if content == 'exit':
#             break
#         start = time()
#         try:
#             soup = submit(url, content)
#         except:
#             print('网络连接错误，请检查您的网络设置')
#         else:
#             input_results(soup)
#         end = time()
#         print ('用时 {}秒'.format(end - start))
#
# if __name__ == '__main__':
#     main()
#
#
import os
import re
import shutil
from concurrent.futures import ThreadPoolExecutor
os.chdir('E:/BaiduYunDownload/李杰的分享/老男孩python全栈3期')
print(os.listdir())
for i in os.listdir():
    if os.path.isfile(i):
        pass
    #     reg = re.compile('python.*?\.mp4|python.*?\.avi')
    #     name = reg.findall(i)[0]
    #     os.renames(i, name)
    if os.path.isdir(i):
        # print('is dir', i)
        os.chdir(i)
        for n in os.listdir():
            reg = re.compile('day\d+')
            name = reg.findall(i)[0] + '-' + n
            print(name)
            # os.renames(n, name)
        os.chdir('..')
