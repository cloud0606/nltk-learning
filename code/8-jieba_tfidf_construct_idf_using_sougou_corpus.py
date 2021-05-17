import os
import codecs
import jieba
import re
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer  
import time

documents = []
terms = [''] * 1000000
textnames = []
stopwords = ['(',')','，','。','？','“','”','‘','’','：','；','【','】','…','<','>','《','》','！']
# Sogou_class=['08','10']
Sogou_class=['08']
m=0
for sc in Sogou_class:
        dirname1 = r"D:\github\nltk-learning\code\sougou\C0000"+sc+"\\"
        files = os.listdir(dirname1)
        fm=0
        for fn in files:
                try:
                        f = codecs.open(dirname1+fn,mode='r')
                        text = f.readlines()
                        f.close()
                        voca=[]
                        for t in text:
                                words = re.sub(r'[\r\t\n\u3000]','',t)
                                words = list(jieba.cut(words))
                                words = [w for w in words if (w not in stopwords) and (len(w) > 0) and (re.search(r'^\D',w))]
                                voca = voca + words
                                terms[m:m+len(words)] = words
                                m = m + len(words)
                        documents.append(' '.join(voca))
                        textnames.append(dirname1 + fn)
                        fm += 1
                except:
                        continue
                if fm > 1000:
                        break


time_start=time.time()
vectorizer = CountVectorizer(min_df=10, token_pattern='(?u)\\b\\w+\\b')  # 定义计数器  
tf = vectorizer.fit_transform(documents)  # 计算TF

transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值
tfidf = transformer.fit_transform(tf)  # fit_transform计算tf-idf，fit_transform将文本转为词频矩阵 

word = vectorizer.get_feature_names() #获取词袋模型中的所有词语
tfidf_val = tfidf.toarray()
# tfidf_sorted = np.argsort(tfidf.toarray(), axis=1)
# 获取对应文本的关键词
# print(documents[0])
print("--- 提取关键词 ---")
worddic = {}
for i in range(len(documents[0])):
        worddic[word[i]] = tfidf_val[0][i]
keywords = sorted(worddic, key=lambda x:worddic[x], reverse=True)
print(keywords)
for i in range(len(keywords))[:30]:
        print(keywords[i],worddic[keywords[i]])

time_end=time.time()
print('time cost',time_end-time_start,'s')