import csv
import pymysql
import you_get
# def canshu():
#     position_info = []
#     with open('me.csv', 'r', encoding='utf-8') as f:
#         reader = csv.reader(f)
#         for line in reader:
#             if reader.line_num == 1:
#                 continue
#             a = line[0], line[1], line[2], line[3], line[4], line[5]
#             position_info.append(a)
#             # print(type(a))
#     return position_info
# test
db = pymysql.connect(host="127.0.0.1", user="root", password="password", db="meituan", charset="utf8")
cursor = db.cursor()
sql = "SELECT * FROM shangjia_info"
cursor.execute(sql)
is_del = cursor.fetchall()
for i in is_del:
    sql_cai = "SELECT * FROM caiping_info WHERE n_id=%s"
    cursor.execute(sql_cai, i[0])
    cai_info = cursor.fetchall()
    print(cai_info)
