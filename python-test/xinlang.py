import urllib.request
import os
import random
import re

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')

    '''

    proxies = ['1.82.216.135:80', '59.107.26.220:10000', '111.13.7.42:81']
    proxy = random.choice(proxies)

    proxy_support = urllib.request.ProxyHandler({'http':proxy})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    '''
    
    response = urllib.request.urlopen(url)
    html = response.read()

    return html


def find_imgs(url):
    html = url_open(url).decode("utf-8")

    p = r'<img src="([^"]+\.jpg)"'
    imglist = re.findall(p, html)

    return imglist
    '''
    img_addrs = []

    a = html.find('img src=')

    while a != -1:
        b = html.find('.jpg', a, a+255)
        if b != -1:
            img_addrs.append(html[a+9:b+4])
        else:
            b = a + 9

        a = html.find('img src=', b)
   
    return img_addrs
    '''
def save_imgs(folder, img_addrs):
   for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)


def download_mm(folder='xinlang', pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = "http://weibo.com/?category=10007"
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_addrs = find_imgs(url)
        save_imgs(folder, img_addrs)

if __name__ == '__main__':
    download_mm()
