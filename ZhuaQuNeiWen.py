import requests
from bs4 import BeautifulSoup
from datetime import datetime
res = requests.get('http://news.sina.com.cn/o/2016-11-22/doc-ifxxwsix4389213.shtml')
res.encoding = 'utf-8'
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
title = soup.select('#artibodyTitle')[0].text # 获取标题
# time = soup.select('.time-source, #navtimeSource')[0].text  #这是自己的方法，获取时间和来源，类型为字符串
timesource = soup.select('.time-source')[0].contents[0].strip() # 老师方法获取时间
dt = datetime.strptime(timesource, '%Y年%m月%d日%H:%M') # 将获取的时间的字符串转为时间表示类型
t = dt.strftime('%Y年%m月%d日') #可以自己设置时间显示方式
laiyuan = soup.select('.time-source span a')[0].text # 获取来源
'''

此为第一种方法：
neirong = soup.select('#artibody p')[:-1] # 获取正文部分，[:-1]表示不要最后的一个标签中的内容
artlist = []
for p in neirong:
    artlist.append(p.text.strip())
wenzhang = '\n  '.join(artlist)
'''

# 这是第二种方法，用一行代码实现，更为简洁

wenzhang = '\n  '.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])
bianji = soup.select('.article-editor')[0].text.lstrip('李鹏') # lstrip('责任编辑：')是从左边将其移除

print(title)
# print(time)
# print(timesource)
# print(dt)
# print(t)
print(laiyuan)
print(wenzhang)
print(bianji)
