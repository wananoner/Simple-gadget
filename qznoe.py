import json
import requests
import logging
import os
import re
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='lqq_qzone.log', level=logging.DEBUG)
url = 'https://user.qzone.qq.com/proxy/domain/m.qzone.qq.com/cgi-bin/new/get_msgb?'
with open('data.json', encoding='utf-8') as f:
    for num, i in enumerate(reversed(list(f))):
        logging.info(f'这是第{num}页留言')
        datas = eval(i)
        for data in reversed(datas['data']['commentList']):
            try:
                name = data['nickname']
                time = data['pubtime']
                info = data['htmlContent']
                info_2 = data['ubbContent'].strip()
                logging.info(f'{time}: {name} say: {info_2}')
                replyList = data['replyList']
                if replyList:
                    logging.info(f'{"="*10}以下为回复内容：')
                    for reply in replyList:
                        content = reply['content']
                        contenter = reply['nick']
                        logging.info(f'\t\t{contenter},Reply:{content}')
            except KeyError:
                logging.warning('这是一条私密评论')

headers = {
    # ':authority':'user.qzone.qq.com',
    # ':method':'GET',
    # ':path':'/proxy/domain/m.qzone.qq.com/cgi-bin/new/get_msgb?uin=583829693&hostUin=610098967&num=10&start=50&hostword=0&essence=1&r=0.024324804308030412&iNotice=0&inCharset=utf-8&outCharset=utf-8&format=jsonp&ref=qzone&g_tk=213132643&qzonetoken=b16f6dddb2bc1878a02fc2d96d079a730fde01e01e6b51eb5947da3b2e5d26bcd38097b958f47933',
    # ':scheme':'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '',
    'referer': 'https://user.qzone.qq.com/123456789?ptlang=2052',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

# a = s.get(url, params=params)
for i in range(90):
    params = {
        'uin': '583829693',
        'hostUin': '303067975',
        'num': '10',
        'start': i*10,
        'hostword': '0',
        'essence': '1',
        # 'r':'0.024324804308030412',
        'iNotice': '0',
        'inCharset': 'utf-8',
        'outCharset': 'utf-8',
        'format': 'jsonp',
        'ref': 'qzone',
        'g_tk': '1995018497',
        'qzonetoken': '49d9abc22e253773ae35dd1fff98105bd317f3787390fs827e6csa82332b06854bf80f0d6985d8c2'
    }
    a = requests.get(url, headers=headers, params=params)

    data = json.loads(a.text[10:-2])
    print('第{}页数据'.format(i), data)

# os.chdir(r'E:\新建文件夹 (2)')
# m_list = os.listdir(r'E:\新建文件夹 (2)')
# all_m = []
# for i in m_list:
#     name_t = re.findall('(.*?)\.(mp3|flac|MP3|wav|ape)', i)[0]
#     name, _t = name_t
#     if name in all_m:
#         print(name, _t)
#         # try:
#         #     os.remove(name + '.mp3')
#         # except FileExistsError:
#         #     os.remove(name + '.MP3')
#     else:
#         all_m.append(name)