import requests
import pprint
import json
import pymysql
import csv
import time

# db = pymysql.connect(host="127.0.0.1", user="root", password="password", db="meituan", charset="utf8")
# cursor = db.cursor()


def all_cai(sj_id):
    # test_url = 'https://takeaway.dianping.com/waimai/ajax/wxwallet/menu?actualLat=&actualLng=&initialLat=34.259458&initialLng=108.947001&geoType=2&mtWmPoiId=2094805&dpShopId=80966797&source=shoplist&_token=eJyVkEtv2zAQhP8LD7pUsChSLxoQAstyXSWi01SW06TIgXpAJvSESVmOiv73Mo3boseeZvbbwWIx38EpKsDShBAirAMplLehYyPkuiaGjg7yfxg2bcWy0yEEy2%2FYgbqN0csb%2BKLmX8Cx4Iv%2B12GkvyciFQBHKQexNAzJ6pJN7HVRcNYNvKsWed8aE%2BMt48Z0mVjTlNJoy268KYbk2A9R4XuQOI5LXK2VV4IgsTxoa6IfT3npC0UbLqTGOy45a2ImfWwtkE0s2%2FsDu8o3obcglguhqbFcju%2FJ31btgf5%2Fj97kfVH66tx5H20JIpuVvId4SJTvQvMTQW%2B804RksvRNhDWgCmn3qhCl9VXZVeVVBa86sATl7WWf1NN4l2LqpbUQh8eQnj8nWXFI1n00e5XwUjTJcD3vZjrJufiapMYuvKtkkj3hlJ7pazJHx8f%2BsiPRhcapSeNyvX6gaBscn52GZ21QsS071Y2V1cGH52aVWxONN1CEm%2FnAz7uY27f77GkMhrGoPw55v3oIXI%2FXFfjxE64XtLU%3D&_=1506522773260'
    url = 'https://takeaway.dianping.com/waimai/ajax/wxwallet/menu?'
    headers = {
        'Host': 'takeaway.dianping.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; PLK-AL10 Build/HONORPLK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN',
        'Referer': 'https://takeaway.dianping.com/waimai/wxwallet?code=001vTIG929EAtO03pSG92nD1H92vTIGn&state=123&',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.8',
        'Cookie': '_hc.v=018814d1-2b04-7113-b352-0c224b5591af.1501688076; m_cookie_issues_uuid=yVsMhGQlPx; _lxsdk=15da39597c12b-0aab3e0fc398e5-20206876-38400-15da39597c321; mter=O-ejUyOTKzBe79Tw378C7V5HIaoAAAAAdAQAAGpwOQCHCVleHrEs8O9ZgaRiH_aN5Cpy58YM53HeT5szkCqQt_zAZG3Gw6WYPAZS6A; ta.uuid=901405955860766817; waimai_cityname=%E5%9F%8E%E5%B8%82%E5%90%8D%E5%B7%B2%E5%88%A0%E9%99%A4; __mta=146757131.1501688076530.1506521098321.1506521252533.10; isUuidUnion=false; dpUserId=""; mtUserId=142481724; _lxsdk_s=6bf8e2bf672f78bb0f481f9542ec%7C%7C80',
    }
    from_data = {
        # 'actualLat': '31.063480025949268',
        # 'actualLng': '121.4983591662249',
        # 'initialLat': '34.259458',
        # 'initialLng': '108.947001',
        'geoType': '2',
        'mtWmPoiId': sj_id['mtWmPoiId'],
        'dpShopId': sj_id['dpShopId'],
        'source': 'shoplist',
        '_token': 'eJxNj82SojAUhd8li950qg0JCFhlTamgBlRaURyY6gUqrYACo5Efp+bdJ6ijru7JuSf5Tv6AI92AloAQwgQCduJaQk0JC5gPWYFg/eIRJCERQbA6Ohpo/SJNBCWCv2pjxs9XoymiL/hUBMNbgvIA2DGWnVqNBvPjwC/86mMT+kkWJtuPdXpoFH548MNGURb+fh+wH+t0E7QREvI5HahY1TvMQiSzuU40Yaji2k/eTsxnQVvA5A1AADjqMK9RWBKhqnILYxFiXAuFQCyLXCkKxPVKINyRrqs6U694AGKC7qF6coMIdVhSIf9WTYhrAp/+Cwlq1HnQIJ18LuZP5n155UL7szN5wP9fuxWAI/rs8HIJPR68tnk8cat0DfI67F7rFG4T0AKBUTpRrJtF1FnMrIZdOu9LZq7cUS52u0agTvXIHqSVYYzUbfSuLXty9FvYjWkSr2ZLITz2Jkj1Ut+zXTues1CgdPp9Tjw9c01L9xqa/FOU8lhOStLpm4sw79PRumcFqPRKzUVmHKlyE3XPfa1/ZE3SzMfT70gz9rnqmkngDMs0r0YiigbVcR7ailudRtY48c7yJTOyqLfYRDSl09WODV17ncdTljvWpavqw0NY2PQS7jUltCeVECwObhv8/Qf0IcMK',
        '_': '1506521305060'

    }
    req = requests.post(url, headers=headers, data=from_data, verify=False)
    req.encoding = 'utf-8'
    # pprint.pprint(req.json())
    a = json.loads(req.text)
    zhonglei = a['data']['categoryList']
    for i in range(len(zhonglei)):
        b = zhonglei[i]['spuList']
        for m in range(len(b)):
            cai_name = str(b[m]['spuName']).strip()  # 商品名称
            short_price = b[m]['currentPrice']  # 小份
            big_price = b[m]['originPrice']  # 大份
            sales = b[m]['saleVolume']  # 月销售
            like_num = b[m]['praiseNum']  # 点赞数
            # print(cai_name, short_price, big_price, sales, like_num)

            # sql = "INSERT INTO caiping_info(n_id, c_name, big_price, short_price, sales, like_num)\
                  # VALUE (%s, %s, %s, %s, %s, %s)"
            # cursor.execute(sql, (sj_id['n_id'], cai_name, big_price, short_price, sales, like_num))

            # db.commit()


def all_shangjia(datas):
    url = 'https://takeaway.dianping.com/waimai/ajax/wxwallet/newIndex?'
    headers = {
        'Host': 'takeaway.dianping.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; PLK-AL10 Build/HONORPLK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN',
        'Referer': 'https://takeaway.dianping.com/waimai/wxwallet?code=001vTIG929EAtO03pSG92nD1H92vTIGn&state=123&',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.8',
        'Cookie': '_hc.v=018814d1-2b04-7113-b352-0c224b5591af.1501688076; m_cookie_issues_uuid=yVsMhGQlPx; _lxsdk=15da39597c12b-0aab3e0fc398e5-20206876-38400-15da39597c321; mter=O-ejUyOTKzBe79Tw378C7V5HIaoAAAAAdAQAAGpwOQCHCVleHrEs8O9ZgaRiH_aN5Cpy58YM53HeT5szkCqQt_zAZG3Gw6WYPAZS6A; ta.uuid=901405955860766817; waimai_cityname=%E5%9F%8E%E5%B8%82%E5%90%8D%E5%B7%B2%E5%88%A0%E9%99%A4; __mta=146757131.1501688076530.1506521098321.1506521252533.10; isUuidUnion=false; dpUserId=""; mtUserId=142481724; _lxsdk_s=6bf8e2bf672f78bb0f481f9542ec%7C%7C80',
    }
    try:
        for data in datas:
            from_data = {
                'startIndex': '0',
                'sortId': '',
                'secondcategoryid': '0',
                'rankTraceId': '',
                'multifilterids': '',
                'lng': data[5],
                'lat': data[4],
                'initialLng': data[5],
                'initialLat': data[4],
                'geoType': '2',
                'firstcategoryid': '0',
                'channel': '24',
                'cateId': '',
                'address': data[1],
                'actualLng': '',
                'actualLat': '',
                '_token': 'eJxNj82SojAUhd8li950qg0JCFhlTamgBlRaURyY6gUqrYACo5Efp+bdJ6ijru7JuSf5Tv6AI92AloAQwgQCduJaQk0JC5gPWYFg/eIRJCERQbA6Ohpo/SJNBCWCv2pjxs9XoymiL/hUBMNbgvIA2DGWnVqNBvPjwC/86mMT+kkWJtuPdXpoFH548MNGURb+fh+wH+t0E7QREvI5HahY1TvMQiSzuU40Yaji2k/eTsxnQVvA5A1AADjqMK9RWBKhqnILYxFiXAuFQCyLXCkKxPVKINyRrqs6U694AGKC7qF6coMIdVhSIf9WTYhrAp/+Cwlq1HnQIJ18LuZP5n155UL7szN5wP9fuxWAI/rs8HIJPR68tnk8cat0DfI67F7rFG4T0AKBUTpRrJtF1FnMrIZdOu9LZq7cUS52u0agTvXIHqSVYYzUbfSuLXty9FvYjWkSr2ZLITz2Jkj1Ut+zXTues1CgdPp9Tjw9c01L9xqa/FOU8lhOStLpm4sw79PRumcFqPRKzUVmHKlyE3XPfa1/ZE3SzMfT70gz9rnqmkngDMs0r0YiigbVcR7ailudRtY48c7yJTOyqLfYRDSl09WODV17ncdTljvWpavqw0NY2PQS7jUltCeVECwObhv8/Qf0IcMK',
                '_': '1506521305060'

            }
            req = requests.post(url, headers=headers, data=from_data, verify=False)
            a = json.loads(req.text)
            try:
                mtPoiNumber = a['data']['mtPoiNumber']
                number = int(mtPoiNumber) // 25 * 25 + 1
                # print(mtPoiNumber)
                # print('*' * 200)
                for num in range(0, number, 25):
                    # startIndex 字段是显示商家的数量，以[0, 25, 50, 75, 100.....]这样递增
                    from_data = {
                        'startIndex': num,
                        'sortId': '',
                        'secondcategoryid': '0',
                        'rankTraceId': '',
                        'multifilterids': '',
                        'lng': data[5],
                        'lat': data[4],
                        'initialLng': data[5],
                        'initialLat': data[4],
                        'geoType': '2',
                        'firstcategoryid': '0',
                        'channel': '24',
                        'cateId': '',
                        'address': data[1],
                        'actualLng': '',
                        'actualLat': '',
                        '_token': 'eJxNj82SojAUhd8li950qg0JCFhlTamgBlRaURyY6gUqrYACo5Efp+bdJ6ijru7JuSf5Tv6AI92AloAQwgQCduJaQk0JC5gPWYFg/eIRJCERQbA6Ohpo/SJNBCWCv2pjxs9XoymiL/hUBMNbgvIA2DGWnVqNBvPjwC/86mMT+kkWJtuPdXpoFH548MNGURb+fh+wH+t0E7QREvI5HahY1TvMQiSzuU40Yaji2k/eTsxnQVvA5A1AADjqMK9RWBKhqnILYxFiXAuFQCyLXCkKxPVKINyRrqs6U694AGKC7qF6coMIdVhSIf9WTYhrAp/+Cwlq1HnQIJ18LuZP5n155UL7szN5wP9fuxWAI/rs8HIJPR68tnk8cat0DfI67F7rFG4T0AKBUTpRrJtF1FnMrIZdOu9LZq7cUS52u0agTvXIHqSVYYzUbfSuLXty9FvYjWkSr2ZLITz2Jkj1Ut+zXTues1CgdPp9Tjw9c01L9xqa/FOU8lhOStLpm4sw79PRumcFqPRKzUVmHKlyE3XPfa1/ZE3SzMfT70gz9rnqmkngDMs0r0YiigbVcR7ailudRtY48c7yJTOyqLfYRDSl09WODV17ncdTljvWpavqw0NY2PQS7jUltCeVECwObhv8/Qf0IcMK',
                        '_': '1506521305060'

                    }
                    req = requests.post(url, headers=headers, data=from_data, verify=False)
                    a = json.loads(req.text)
                    print('*' * 100)
                    # pprint.pprint(a)
                    a_list = a['data']['shopList']

                    for i in range(0, len(a_list)):
                        try:
                            huodong = ','.join([x['actDesc'] for x in a_list[i]['activityList']])
                        except:
                            huodong = None
                        name = a_list[i]['name']
                        qisongjia = a_list[i]['minFee']
                        peisongfei = a_list[i]['minDeliverFee']
                        mtWmPoiId = a_list[i]['mtWmPoiId']
                        dpShopId = a_list[i]['id']
                        sold = a_list[i]['sold']  # 月销售
                        # print(huodong, name, qisongjia, peisongfei, mtWmPoiId, dpShopId, sold)

                        # sql_insert = "INSERT INTO shangjia_info(d_name, qisong_pice, peisong_pice, mtwmpoi_id,\
                        #              dpShop_id, sold, huodong, address_type, address_name, quyu, address)\
                        #               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        # cursor.execute(sql_insert, (name, qisongjia, peisongfei, mtWmPoiId, dpShopId, sold, huodong,
                        #                             data[0], data[1], data[2], data[3]))
                        # n_id = cursor.lastrowid
                        # db.commit()
                        sj_id = {'mtWmPoiId': mtWmPoiId,
                                 'dpShopId': dpShopId,
                                 'n_id': n_id}
                        all_cai(sj_id)
            except Exception as e:
                print('@'*100, str(e))
                    # print('变更商家， 等待10s')
        #         time.sleep(10)
        #     print('变更商家列表， 等待10s')
        #     time.sleep(10)
        # print('变更地址， 等待30s')
        # time.sleep(30)
    except Exception as e:
        print('!'*100, str(e))


def canshu():
    position_info = []
    with open('me.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for line in reader:
            if reader.line_num == 1:
                continue
            a = line[0], line[1], line[2], line[3], line[4], line[5]
            position_info.append(a)
            # print(type(a))
    return position_info


all_shangjia(canshu())
