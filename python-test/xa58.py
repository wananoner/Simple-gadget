# -*-coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from lxml import etree

def open_url(url):          #打开url，获取网页代码
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    html = requests.get(url, headers=headers)
    html.encoding = 'utf-8'
    selector = etree.HTML(html.text)
    return selector

def introduce(selector):    #定位标题位置并获取标题地址url
    sites = selector.xpath('//div[@class="maincon"]/div/dl')
    address = []
    for site in sites:
        title = ''.join(site.xpath('dt/a/text()'))
        new_url = site.xpath('dt/a/@href')
        address.append(''.join(new_url))
        #print(title)
    return address

def content(url):         #进入标题地址抓取页面内容  
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.select('.headConLeft')[0].text
    name = soup.select('.posSumLeft')[0].text
    money = soup.select('.posinfo')[0].text
    print(title, name, money)

def perform(url):       #执行函数
    selector = open_url(url)
    url_list = introduce(selector)
    for url in url_list:
        content(url)
    
def main():             #主函数
    url = 'http://xa.58.com/renli/?key=%E6%96%87%E5%91%98&cmcskey=%E6%96%87%E5%91%98&final=1&jump=1&specialtype=gls'
    try:
        perform(url)
    except:
        print("网络连接错误，请检查您的网络设置")
    else:
        content = input("如需查看下一页请按:y,否则请按任意键退出 ")
        if content == 'y':
            for page in range(2, 20):
                new_url = 'http://xa.58.com/renli/pn' + str(page) + '/?key=%E6%96%87%E5%91%98&cmcskey=%E6%96%87%E5%91%98&final=1&jump=1&specialtype=gls&PGTID=0d303652-001e-322f-0a03-3f8664226838&ClickID=3'
                perform(new_url)
                content = input("如需查看下一页请按:y,否则请按任意键退出 ")
                if content != 'y':
                    break        
    
if __name__ == '__main__':
    main()
