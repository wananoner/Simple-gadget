import urllib.request
import random

url = 'http://www.whatismyip.com.tw'

iplist = ['211.143.146.235:80', '1.82.216.135:80', '111.13.7.42:81', '1.82.216.134:80']

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')]

urllib.request.install_opener(opener)

respone = urllib.request.urlopen(url)
html = respone.read().decode('utf-8')

print(html)
