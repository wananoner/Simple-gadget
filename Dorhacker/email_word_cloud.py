"""
    去 Gmail 收件箱获取所有邮件内容
    链接：'https://www.googleapis.com/auth/gmail.modify'
    此外，client_secret.json应该保存在与此文件相同的目录中
"""

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import jieba.analyse


def read_all_email(GMAIL, label_id):
    # SENT 发件箱、
    # 获取收件箱信息字典
    user_id = 'me'  # 用户id
    unread_msgs = GMAIL.users().messages().list(userId='me', labelIds=[label_id]).execute()
    print(unread_msgs)
    if 'messages' in unread_msgs:
        # 获取一个字典，现在读取关键“消息”的值
        mssg_list = unread_msgs['messages']

        print("读取邮件数量: ", str(len(mssg_list)))

        all_email_info = []
        num = 1
        for mssg in mssg_list:
            m_id = mssg['id']  # 获取个人消息的ID
            message = GMAIL.users().messages().get(userId=user_id, id=m_id).execute()  # 使用API获取消息
            print('正在读取第 %s 封邮件，请稍后...' % num)
            # print(message['snippet'])
            all_email_info.append(message['snippet'])
            num += 1
            # with open('email_info.txt', 'wb') as f:
            #     f.write(''.join(all_email_info).encode('utf-8'))
    else:
        print('没有数据')


def read_email_info():
    # 创建具有身份验证详细信息的storage.JSON文件, 此为Google Gmail API
    # 连接地址
    SCOPES = 'https://www.googleapis.com/auth/gmail.modify'
    store = file.Storage('storage.json')
    creds = store.get()
    print(creds)
    if not creds.access_token_expired:
        creds = creds.refresh(Http())

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))

    label_id = 'INBOX'

    read_all_email(GMAIL, label_id)


def keyword_dict():
    # 读取存放用户邮件内容的 email_info.txt 文件
    text_from_file_with_apath = open('email_info.txt', encoding='utf-8').read()
    # 精确分词，返回列表
    wordlist_after_jieba = jieba.lcut(text_from_file_with_apath, cut_all=False)
    # 读取存放中文停用词表的 TextBayes.txt 文件
    TextBayes = open('TextBayes.txt', encoding='utf-8').read().splitlines()
    key = []
    num = []
    # 将分词结果对照中文停用词表剔除
    for i in range(0, len(wordlist_after_jieba)):

        if len(wordlist_after_jieba[i].strip()) > 2:
            if wordlist_after_jieba[i] not in key and wordlist_after_jieba[i] not in TextBayes:
                key.append(wordlist_after_jieba[i])
                num.append(wordlist_after_jieba.count(wordlist_after_jieba[i]))
    # 关键词和出现频率存放在字典中
    word_cloud = dict(zip(key, num))
    print(word_cloud)

    return word_cloud


read_email_info()
# print(keyword_dict())
# a = open('word_cloud.json')
