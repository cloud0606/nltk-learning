import os
import codecs
import jieba
import re
from sklearn import feature_extraction  
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer  
import numpy as np
from scipy import spatial
from scipy.cluster.vq import kmeans,vq,whiten

documents = []
terms = [''] * 1000000
textnames = []
stopwords = ['(',')','，','。','？','“','”','‘','’','：','；','【','】','…','<','>','《','》','！']
Sogou_class=['08','10']
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
'''
def tfidf_fun(documents,stopwords):
        word=[]
        
        return tf, tfidf,wordlist
'''
vectorizer = CountVectorizer(min_df=10, token_pattern='(?u)\\b\\w+\\b')  # 定义计数器  
transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值

tf = vectorizer.fit_transform(documents)  # 计算TF
tfidf = transformer.fit_transform(tf)  # fit_transform计算tf-idf，fit_transform将文本转为词频矩阵 
word = vectorizer.get_feature_names()
tfmat = tf.toarray()

from sklearn.decomposition import TruncatedSVD

svd = TruncatedSVD(n_components=300)
svd.fit(tfidf)  
features = svd.fit_transform(tfidf)

import sklearn
# 向量间余弦距离
dm = sklearn.metrics.pairwise.cosine_similarity(features, dense_output=True)

max_dist = -1
max_file = [0,0]
for n in range(len(dm) - 1):
        for m in range(n + 1, len(dm)):
                if dm[n,m] > max_dist:
                        max_dist = dm[n, m]
                        max_file = [n, m]

print(textnames[max_file[0]])
print(textnames[max_file[1]])
