import requests
from lxml import etree
import re
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import csv


def jd():
    browser = webdriver.Chrome()
    url = 'https://search.jd.com/Search?keyword=%E7%99%BD%E9%85%92&enc=utf-8&wq=%E7%99%BD%E9%85%92&pvid=91cc689c20be4ae79df9e94ebe6adc60'
    browser.get(url)

    for i in range(100):
        html = browser.page_source
        selector = etree.HTML(html)
        moneys = [''.join(i.xpath('div/div[2]/strong/i/text()')) for i in
                  selector.xpath('//*[@id="J_goodsList"]/ul/li')]
        names = [''.join(i.xpath('div/div[3]/a/em/text()')) for i in selector.xpath('//*[@id="J_goodsList"]/ul/li')]
        pintjias = [''.join(i.xpath('div/div[4]/strong/a/text()')) for i in
                    selector.xpath('//*[@id="J_goodsList"]/ul/li')]

        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[9]/em').click()
        header = ['name', 'money', 'pinjia']
        html = browser.page_source
        header = ['name', 'money', 'pinjia']
        if i % 2 != 0:
            print(moneys)
            print(names)
            print(pintjias)
            print(len(moneys))
            print(len(names))
            print(len(pintjias))
            # for name, money, pintjia in zip(names, moneys, pintjias):
            #     rows = [name, money, pintjia]
            #     with open('dog.csv', 'a', encoding='utf-8') as f:
            #         f_csv = csv.writer(f, delimiter=',', lineterminator='\n')
            #         f_csv.writerow(rows)
    browser.quit()


def taobao():
    browser = webdriver.Chrome()
    url = 'https://s.taobao.com/search?q=%E7%99%BD%E9%85%92&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'
    browser.get(url)
    for i in range(50):
        html = browser.page_source
        # with open('das.html', encoding='utf-8') as f:
        #     html = f.read()

        selector = etree.HTML(html)
        price = selector.xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div/div[2]/div[1]/div[1]/strong/text()')
        name = [''.join(i.xpath('div[2]/a/text()')) for i in selector.xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div/div[2]')]
        month_c = selector.xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div/div[2]/div[1]/div[2]/text()')
        # comment = selector.xpath('//*[@id="J_ItemList"]/div/div/p[3]/span[2]/a/text()')
        print(price)
        print(name)
        print(month_c)
        # print(comment)
        print(len(price))
        print(len(name))
        print(len(month_c))
        # # print(len(comment))
        # print(selector.xpath('//b[@class="ui-page-num"]/a[last()]/text()'))
        # time.sleep(1)
        for money, name, pintjia in zip(price, name, month_c):
            # print(i, ''.join(j.split()), k)
            rows = [''.join(name.split()), money, pintjia]
            with open('taobao.csv', 'a', encoding='utf-8') as f:
                f_csv = csv.writer(f, delimiter=',', lineterminator='\n')
                f_csv.writerow(rows)

        try:
            browser.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/ul/li[last()]/a/span[1]').click()
            WebDriverWait(browser, 2).until(
                EC.presence_of_element_located((By.CLASS_NAME, "J_Ajax num icon-tag"))
            )
        except Exception as e:
            print(e)

    browser.quit()


def tianmao():
    browser = webdriver.Chrome()
    url = 'https://list.tmall.com/search_product.htm?q=%B0%D7%BE%C6&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton'
    browser.get(url)
    for i in range(100):
        html = browser.page_source
        # with open('das.html', encoding='utf-8') as f:
        #     html = f.read()
        selector = etree.HTML(html)
        price = selector.xpath('//*[@id="J_ItemList"]/div/div/p[1]/em/text()')
        name = [''.join(i.xpath('a/text()')) for i in selector.xpath('//*[@id="J_ItemList"]/div/div/p[2]')]
        month_c = selector.xpath('//*[@id="J_ItemList"]/div/div/p[3]/span[1]/em/text()')
        comment = selector.xpath('//*[@id="J_ItemList"]/div/div/p[3]/span[2]/a/text()')
        try:
            browser.find_element_by_xpath('//*[@id="content"]/div/div[8]/div/b[1]/a[last()]').click()
            WebDriverWait(browser, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, "ui-page-next"))
            )
        except Exception as e:
            print(e)
        if i % 2 != 0:
            print(price)
            print(name)
            print(month_c)
            print(comment)
            print(len(price))
            print(len(name))
            print(len(month_c))
            print(len(comment))
            for p, j, k, l in zip(price, name, month_c, comment):
                # print(i, ''.join(j.split()), k, l)
                rows = [''.join(j.split()), p, k, l]
                with open('cat.csv', 'a', encoding='utf-8') as f:
                    f_csv = csv.writer(f, delimiter=',', lineterminator='\n')
                    f_csv.writerow(rows)
    browser.quit()
