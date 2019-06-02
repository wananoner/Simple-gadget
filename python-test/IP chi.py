# -*- coding: utf-8 -*-
import urllib.request
import re
import os

def url_open(url):
        
    req = urllib.request.Request(url)
    req.add_header('user-agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')# 或者等会解码
    print(html)

    return html

def get_imgs(url):
    html = url_open(url)
    p = r'<img width="190" height="190" data-img="1" src="([^"]+\.jpg)"'
    imlist = re.findall(p, html)
    print(imlist)

    return imlist

def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)

def main(folder='jingdong'):
    url = 'https://list.jd.com/list.html?cat=1315,1342,12003'
    img_addrs = get_imgs(url)
    save_imgs(folder, img_addrs)

if __name__ == '__main__':
    main()
    
