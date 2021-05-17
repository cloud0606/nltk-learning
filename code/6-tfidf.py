# from gensim.models import TfidfModel
# print(text1)
# model = TfidfModel(text1) # fit model
# vector = model[text1[0]] # apply model to the first corpus document

from nltk.book import *
from sklearn import feature_extraction  
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer  
corpus = text1
vectorizer = CountVectorizer(min_df=1, token_pattern='(?u)\\b\\w+\\b')#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频  
transformer = TfidfTransformer()#该类会统计每个词语的tf-idf权值  
tf = vectorizer.fit_transform(corpus) # 计算词频
tfidf = transformer.fit_transform(tf)#fit_transform计算tf-idf，fit_transform将文本转为词频矩阵  

words = vectorizer.get_feature_names()#获取词袋模型中的所有词语  
weight = tfidf.toarray()#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重  
#比较tf与tfidf向量各维度的值，可以看到，tfidf加重了低频词的权重，起到了突出主题的作用。