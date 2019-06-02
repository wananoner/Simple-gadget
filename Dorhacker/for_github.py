'''
This script does the following:
- Go to Gmal inbox
- Find and read all the unread messages
- Extract details (Date, Sender, Subject, Snippet, Body) and export them to a .csv file / DB
- Mark the messages as Read - so that they are not read again
此脚本执行以下操作：
- 去Gmal收件箱
- 查找并读取所有未读消息
- 提取详细信息（日期，发件人，主题，代码段，正文）并将其导出到.csv文件/数据库
- 将邮件标记为已读 - 以使其不再读取
'''

'''
Before running this script, the user should get the authentication by following 
the link: https://developers.google.com/gmail/api/quickstart/python
Also, client_secret.json should be saved in the same directory as this file
在运行此脚本之前，用户应该通过以下方式获取身份验证
链接：https：//developers.google.com/gmail/api/quickstart/python
此外，client_secret.json应该保存在与此文件相同的目录中
'''

# Importing required libraries
from apiclient import discovery
from apiclient import errors
from httplib2 import Http
from oauth2client import file, client, tools
import base64
from bs4 import BeautifulSoup
import re
import time
import dateutil.parser as parser
import requests
from datetime import datetime
import datetime
import csv

# 创建具有身份验证详细信息的storage.JSON文件
# 我们正在使用修改而不是只读，因为我们将标记消息Read
SCOPES = 'https://www.googleapis.com/auth/gmail.modify'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))
print(GMAIL)
user_id = 'me'
label_id_one = 'INBOX'
label_id_two = 'UNREAD'

# 从Inbox获取所有未读邮件
# labelIds可以相应更改

unread_msgs = GMAIL.users().messages().list(userId='me', labelIds=[label_id_one]).execute()

# 我们得到一个字典，现在读取关键“消息”的值
mssg_list = unread_msgs['messages']
print(mssg_list)
print(len(mssg_list))
print("收件箱中所有邮件数量: ", str(len(mssg_list)))

final_list = []

for mssg in mssg_list:
    temp_dict = {}
    m_id = mssg['id']  # 获取个人消息的ID
    message = GMAIL.users().messages().get(userId=user_id, id=m_id).execute()  # 使用API获取消息
    print('Message snippet: %s' % message['snippet'])
    # payld = message['threadId']  # 获取消息的有效载荷
    # headr = payld['headers']  # 获取有效载荷的标题
#
#     # print(m_id)
#     # print(payld)
#     # print(message)
#     for one in headr:  # 获取主题
#         if one['name'] == 'Subject':
#             msg_subject = one['value']
#             temp_dict['Subject'] = msg_subject
#         else:
#             pass
#
#     for two in headr:  # 获取时间
#         if two['name'] == 'Date':
#             msg_date = two['value']
#             date_parse = (parser.parse(msg_date))
#             m_date = (date_parse.date())
#             temp_dict['Date'] = str(m_date)
#         else:
#             pass
#
#     for three in headr:  # 获取发件人
#         if three['name'] == 'From':
#             msg_from = three['value']
#             temp_dict['Sender'] = msg_from
#         else:
#             pass
#
#     temp_dict['Snippet'] = message['snippet']  # fetching message snippet
#
#     try:
#
#         # Fetching message body
#         mssg_parts = payld['parts']  # fetching the message parts
#         part_one = mssg_parts[0]  # fetching first element of the part
#         part_body = part_one['body']  # fetching body of the message
#         part_data = part_body['data']  # fetching data from the body
#         clean_one = part_data.replace("-", "+")  # decoding from Base64 to UTF-8
#         clean_one = clean_one.replace("_", "/")  # decoding from Base64 to UTF-8
#         clean_two = base64.b64decode(bytes(clean_one, 'UTF-8'))  # decoding from Base64 to UTF-8
#         soup = BeautifulSoup(clean_two, "lxml")
#         mssg_body = soup.body()
#         # mssg_body is a readible form of message body
#         # depending on the end user's requirements, it can be further cleaned
#         # using regex, beautiful soup, or any other method
#         temp_dict['Message_body'] = mssg_body
#
#     except:
#         pass
#
#     print(temp_dict)
# final_list.append(temp_dict)  # This will create a dictonary item in the final list
#
#     # This will mark the messagea as read
#     GMAIL.users().messages().modify(userId=user_id, id=m_id, body={'removeLabelIds': ['UNREAD']}).execute()
#
# print("Total messaged retrived: ", str(len(final_list)))
#
# '''
# The final_list will have dictionary in the following format:
# {	'Sender': '"email.com" <name@email.com>',
# 	'Subject': 'Lorem ipsum dolor sit ametLorem ipsum dolor sit amet',
# 	'Date': 'yyyy-mm-dd',
# 	'Snippet': 'Lorem ipsum dolor sit amet'
# 	'Message_body': 'Lorem ipsum dolor sit amet'}
# The dictionary can be exported as a .csv or into a databse
# '''
#
# # exporting the values as .csv
# with open('CSV_NAME.csv', 'w', encoding='utf-8', newline='') as csvfile:
#     fieldnames = ['Sender', 'Subject', 'Date', 'Snippet', 'Message_body']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
#     writer.writeheader()
#     for val in final_list:
#         writer.writerow(val)
