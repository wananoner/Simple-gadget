# -*-conding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from lxml import etree
import os

# 输出所在网址的内容
def introduce(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.select('h1')[0].text
    content = '\n  '.join([p.text.strip() for p in soup.select('.section')])
    #print(title)
    #print(content)
    with open('python.doc', 'a+', encoding='utf-8') as f:
        f.write(content)
# 返回目录所对应的地址
def get_url(selector):
    sites = selector.xpath('//div[@class="toctree-wrapper compound"]/ul/li')
    address = []
    for site in sites:
        directory = ''.join(site.xpath('a/text()'))
        new_url = site.xpath('a/@href')
        address.append('http://www.pythondoc.com/pythontutorial3/' + ''.join(new_url))
    return address

def main(): 
    url = 'http://www.pythondoc.com/pythontutorial3/index.html#'
    html = requests.get(url)
    html.encoding = 'utf-8'
    selector = etree.HTML(html.text)
    introduce(url)
    url_list = get_url(selector)
    for url in url_list:
        introduce(url)

if __name__ == '__main__':
    main()
