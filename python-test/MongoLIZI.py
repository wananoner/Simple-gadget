# -*- coding: utf-8 -*-
import pymongo

# 以下三行命令是创建python到数据库mongodb的连接
connection = pymongo.MongoClient() # 在本机运行括号里不需要写内容
tdb = connection.jikexueyuan #jikexueyuan是命名的名称，可更改
post_info = tdb.test # 同jikexueyuan一样

jike = {'name':'jike', 'age':'5', 'skill':'Python'}
god = {'name':'我爱的人', 'age':'21', 'skill':'love me', 'other':'我也是哈'}
godslaver = {'name':'月老', 'age':'unknow', 'other':'管我什么事'}

#以下三条是添加
post_info.insert(jike)
post_info.insert(god)
post_info.insert(godslaver)
# 这一条是删除
post_info.remove({'name':'极客'})

# 测试使用， 无关紧要
print('操作数据库成功')
