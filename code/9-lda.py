from gensim.models import LdaModel
import pandas as pd
from gensim.corpora import Dictionary
import jieba
import time

time_start=time.time()
# 数据预处理
with open("toutiao_cat_data.txt","r",encoding="utf-8") as f:
# with open("test.txt","r",encoding="utf-8") as f:
    data = []
    for line in f.readlines():
        line = line.strip()  # 去除空格
        line = ','.join(line.split("_!_")[3:])  # 按符号切割数据，并且不要前三个无关文本内容的数据
        data.append(jieba.lcut(line))

# 文本向量化
dictionary = Dictionary(data)  # 统计每个词在其它文本中出现了多少次
dictionary.filter_n_most_frequent(200)  # 过滤掉频率过高的词
corpus = [dictionary.doc2bow(text) for text in data ]  # 转化为词袋向量

# 训练模型
lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=10)  # 指定了10个主题，

# 获取主题词分布
topic_list = lda.print_topics(20)
# print(topic_list)
for i in topic_list:
    print(i)

def pre(data):
    '获取某篇文档的主题分布'
    print(data)
    doc_bow = dictionary.doc2bow(data)  # 文档转换成bow
    doc_lda = lda[doc_bow]
    print(doc_lda)


# 获取某篇文档的主题分布
for i in [56,1003,3000]:
    pre(data[i])



