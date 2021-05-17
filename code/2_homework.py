# 1. 使用正则表达式编程计算Moby Dick（NLTK.Book导入
# 的text1）文本中，26个字母结尾词的各自次数。
# 2. 文件28885.txt是一篇小说，请用re提取出书名，作者
# 名字，语言，以及小说正文。
# 3. 从email文件中，提取收件人和接收人的email，主题，
# 以及附件的文件名。
# re.search('^[a-z]*m.r.ing$',w)
# re.search('^[a-z]?m.r.ing$',w)
# re.search('^[a-z]+m.r.ing$',w)
from nltk.book import *
import re

# 1
count = 0
cdic = dict()
for w in text1:
    m = re.match("[a-zA-Z]$",w)
    if m :
        c = w[-1:]
        if c in cdic.keys():
            cdic[w[-1:]] += 1
        else:
            cdic[w[-1:]] = 1
    if count == 20:
        break
for key, val in cdic.items():
    print(key, val)
