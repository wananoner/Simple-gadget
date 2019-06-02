# -*-coding : utf-8 -*-
import time
from lxml import etree
from bs4 import BeautifulSoup
from selenium import webdriver

def moni(url, content):    
    browser = webdriver.PhantomJS()
    #browser = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
    browser.get(url)
    browser.implicitly_wait(30) # 智能等待页面加载完成
    browser.find_element_by_id("live-search").send_keys(content+'\n')   # 输入信息跳转
    browser.find_element_by_partial_link_text(content).click()  # 匹配输入内容的公司名称，进入
    browser.implicitly_wait(30)
    browser.switch_to_window(browser.window_handles[-1])    # 捕获最新窗口
    browser.implicitly_wait(30)
    # 获取数据
    soup = BeautifulSoup(browser.page_source, 'lxml')
    company = soup.select('div[class="in-block ml10 f18 mb5 ng-binding"]')[0].text
    tag_shareholders = soup.select('th[width="22%"]')[0].text
    tag_percent = soup.select('th[width="12%"]')[0].text
    tag_money = soup.select('th[width="33%"]')[0].text
    name = soup.select('a[event-name="company-detail-investment"]')
    percent = soup.select('span[class="c-money-y ng-binding"]')
    money = soup.select('''span[ng-class="item.amomon?'':'c-none'"]''')
    print(company)
    print(tag_shareholders, tag_percent, tag_money)
    for names, percents, moneys in zip(name, percent, money):
        print(names.text, percents.text, moneys.text)
    browser.implicitly_wait(30)
    browser.quit()
    
def main():
    url = "http://www.tianyancha.com/search"
    content = input("请输入需要查询公司的名称： ")
    moni(url, content)
    
if __name__ == "__main__":
    main()



