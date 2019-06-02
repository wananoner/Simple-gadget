# -*-coding: utf-8-*-
import urllib.request

url = 'http://www.gsxt.gov.cn/index.html'
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11')
proxy = '125.88.74.122:83'
proxy_support = urllib.request.ProxyHandler({'http':proxy})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read()

print(html)
