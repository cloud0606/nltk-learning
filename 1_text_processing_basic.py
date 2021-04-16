from nltk.book import *
# 1. 制作《理智与情感》中四个主角：Elinor，Marianne，Edward 和
# Willoughby 的分布图。在这部小说中关于男性和女性所扮演的不同角
# 色，你能观察到什么？你能找出一对夫妻吗？
# 女性角色 Elinor和 Marianne 角色出场率高，贯穿全文。两位男性角色基本是交替出现，不同时在场。
# 夫妻可能是 Elinor 和 Edward ，或者  Marianne 和 Willoughby，出错时间段大致吻合


text2.dispersion_plot(['Elinor', 'Marianne', 'Edward', 'Willoughby'])
# 2. 写一个小程序文件 Least_common_multiple，计算两个数的最小公倍
# 数,写一个表达式提取 text2 中最后一个词，两个词。


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def lcm(x, y):
    lcm = (x*y)//gcd(x, y)
    return lcm


# print(lcm(3, 7))
# print(lcm(5, 15))
print(text2[-2:])

# 3. 使用for 和if 语句组合循环遍历《巨蟒和圣杯》（text6）的电影剧本中
# 的词，输出所有的大写词作为一个列表，如果是每行输出一个呢？
[w for w in text6 if w.isupper()]
for w in text6 :
    if w.isupper():
        print("%s" % (w))

# 4. 找出聊天语料库（text5）中所有四个字母的词。使用频率分布函数
# （FreqDist），以频率从高到低显示这些词。
FreqDist([w for w in text5 if len(w) == 4])

# 5. 写表达式找出text6 中所有符合下列条件的词。要求结果是词链表的形式：
# ['word1', 'word2', ...]。
# a. 以ize 结尾
# b. 包含字母z
# c. 包含字母序列pt
# d. 除了首字母外是全部小写字母的词（即titlecase）
[w for w in text6 if w.endswith('ize')]
[w for w in text6 if 'z' in w]
[w for w in text6 if 'pt' in w]
[w for w in text6 if w.istitle()]

# 6. 定义sent 为词链表['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']。编写代码
# 执行以下任务：
#   a. 输出所有sh 开头的单词
#   b. 输出所有长度超过4个字符的词
sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
[w for w in sent if w.startswith('sh')]
[w for w in sent if len(w) > 4]

# 7. 下面的 Python 代码是做什么的？sum([len(w) for w in text1])，如何用它来算出一个文本的平均词长？
# 计算text1中所有词长的总和，该值除以词数可算的平均词长
sum([len(w) for w in text1]) / len(text1)

# 8. 定义一个名为vocab_size(text)的函数，以文本作为唯一的参数，返回文本的词汇量。
def vocab_size(text):
    return len(set(text))


vocab_size(text1)
vocab_size(text2)


# 9. 定义一个函数percent(word, text)，计算一个给定的词在文本中出现的频率，结果以百分比表示。
def percent(word, text):
    fd1 = FreqDist(text1)
    return f'{fd1[word] / len(text) * 100:.3}% '


percent("the", text1)
percent("that", text1)

# 找使用最多的标签
tags = [tag]

#