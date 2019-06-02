import jieba.analyse
import matplotlib.pyplot as plt
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False


def keyword_dict():
    # 读取存放用户邮件内容的 email_info.txt 文件
    text_from_file_with_apath = open('email_info.txt', encoding='utf-8').read()
    # 精确分词，返回列表
    wordlist_after_jieba = jieba.lcut(text_from_file_with_apath, cut_all=False)
    TextBayes = open('TextBayes.txt', encoding='utf-8').read().splitlines()
    key = []
    num = []
    for i in wordlist_after_jieba:
        if len(i) > 0:
            if i not in key and i not in TextBayes:
                key.append(i)
                num.append(wordlist_after_jieba.count(i))

    word_cloud = dict(zip(key, num))
    name_list = []
    num_list = []
    for k, v in word_cloud.items():
        if v > 100 and k.split():
            name_list.append(k)
            num_list.append(v)

    rects = plt.bar(range(len(num_list)), num_list, color='rgby')
    # X轴标题
    index = range(len(name_list))
    index = [float(c) + 0.4 for c in index]
    plt.ylim(ymax=1000, ymin=0)
    plt.xticks(index, name_list)
    plt.ylabel("arrucay(%)")  # X轴标签
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height) + '%', ha='center', va='bottom')

    plt.show()

    return word_cloud


keyword_dict()

