import jieba
import jieba.analyse
import time

sentence = ""
filename = "sougou_C08_10.txt"
pf = open(filename,"r")
sentence = pf.read()

# 1. tfidf
# topK=20输出前20个关键词，withWeight为是否一并返回关键词权重值，allowPOS：仅包括指定词性的词，
print("--- tfidf --- ")
time_start=time.time()
keywords = jieba.analyse.extract_tags(sentence, topK=20, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
for item in keywords:
    print(item)
time_end=time.time()
print('time cost',time_end-time_start,'s')

# 2.textrank
print("--- textrank ---")
time_start=time.time()
keywords = jieba.analyse.textrank(sentence, topK=20, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v')) 
for item in keywords:
    print(item)

time_end=time.time()
print('time cost',time_end-time_start,'s')