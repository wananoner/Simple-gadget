from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator


def clean_input(in_put):
    in_put = re.sub('\n+', " ", in_put).lower()
    in_put = re.sub('\[[0-9]*\]]', "", in_put)
    in_put = re.sub(' +', " ", in_put)
    in_put = bytes(in_put, 'utf-8')
    in_put = in_put.decode('ascii', 'ignore')
    result = []
    in_put = in_put.split()
    for item in in_put:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower()) == 'a' or item.lower() == 'i':
            result.append(item)
    return result


def nagrams(in_put, n):
    in_put = clean_input(in_put)
    output = {}
    for i in range(len(in_put)-n+1):
        ngramtemp = ''.join(in_put[i:i+n])
        if ngramtemp not in output:
            output[ngramtemp] = 0
        output[ngramtemp] += 1
    return output


content = str(urlopen("http://pythonsctaping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
ngrams = nagrams(content, 2)
sortedNGrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
print(sortedNGrams)