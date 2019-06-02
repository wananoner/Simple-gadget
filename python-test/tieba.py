import urllib.request
import os
import re

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read()

    return html

def get_img(html):
    html = open_url(url).decode('utf-8')
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'
    imglist = re.findall(p, html)

    for each in imglist:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = open_url(each)
            f.write(img)

if __name__ == '__main__':
    url = "http://tieba.baidu.com/p/3563409202/"
    get_img(open_url(url))
    
