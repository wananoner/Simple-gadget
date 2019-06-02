import jieba.analyse


def keyword_dict():
    # 读取存放用户邮件内容的 email_info.txt 文件
    text_from_file_with_apath = open('email_info.txt', encoding='utf-8').read()
    # 精确分词，返回列表
    wordlist_after_jieba = jieba.lcut(text_from_file_with_apath, cut_all=False)
    TextBayes = open('TextBayes.txt', encoding='utf-8').read().splitlines()
    key = []
    num = []
    for i in range(0, len(wordlist_after_jieba)):
        if len(wordlist_after_jieba[i]) > 0:
            if wordlist_after_jieba[i] not in key and wordlist_after_jieba[i] not in TextBayes:
                key.append(wordlist_after_jieba[i])
                num.append(wordlist_after_jieba.count(wordlist_after_jieba[i]))

    word_cloud = dict(zip(key, num))
    print(word_cloud)
    return word_cloud


keyword_dict()