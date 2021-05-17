# 什么是Unicode编码和UTF-8，二者的关系，如何转换？
# Unicode 为世界上所有字符都分配了一个唯一的数字编号，这个编号范围从 0x000000 到 0x10FFFF (十六进制)，有 110 多万，每个字符都有一个唯一的 Unicode 编号，这个编号一般写成 16 进制，在前面加上 U+。
# UTF-8 就是使用变长字节表示,顾名思义，就是使用的字节数可变，这个变化是根据 Unicode 编号的大小有关，编号小的使用的字节就少，编号大的使用的字节就多。使用的字节个数从 1 到 4 个不等。

# 写一个函数，文本是其唯一输入参数，画出该文本的词长—频率分布图
from nltk.book import *
import matplotlib.pyplot as plt
def wordLenFreq(text):
    d = dict() # 用于记录每种词长的频率和
    fd1 = FreqDist(text) # 获取词频
    for (word, count) in fd1.items():
        if len(word) in d.keys():
            d[len(word)] += count # 词长已经在字典中
        else:
            d[len(word)] = count # 词长不在字典中
    d = dict(sorted(d.items(), reverse=False))
    # print(d)
    # print([k for k in d.keys()])
    # print([v for v in d.values()])
    plt.plot([k for k in d.keys()], [v for v in d.values()])
    plt.show()
    return d

wordLenFreq(text1)