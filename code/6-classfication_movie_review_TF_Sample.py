import nltk
from nltk.corpus import movie_reviews
from pylab import plot,show
from numpy import array
from numpy.random import rand
from scipy.cluster.vq import kmeans,vq,whiten
import numpy as np
import random
import collections
import time

time_start=time.time()
# 1.数据格式化，转化为（[词列表的影评]，标签) 二元组
documents = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)	

# 2.特征词选取
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())  # 获取全部影评的词频表
all_words = all_words.most_common(2000)  # 词频表按频率排序
stopwords = nltk.corpus.stopwords.words('english')  # 停词
word_features  = [w for (w,f) in all_words if w not in stopwords]  # 去重停词作为特征 停词有 ['i', 'me', 'my', 'myself', 'we', 

# 计算每个文本的特征
features = np.zeros([len(documents), len(word_features)],dtype=float)  # 分配记录 文本-特征 的大矩阵
for n in range(len(documents)):
        document_words = documents[n][0] # 文本的所有词列表
        pdf = collections.Counter(document_words) #  统计词频，为啥不用FreqDist呢?
        for m in range(len(word_features)):
                if word_features[m] in document_words:
                        features[n,m] = pdf[word_features[m]]

# 3.划分训练集和测试集 前1500是训练集
target=[c for (d,c) in documents]
train_set1=features[:1500,:]
target_train=target[:1500]
test_set1=features[1500:,:]
target_test=target[1500:]

# from sklearn.svm import SVC
# svclf = SVC(kernel ='linear',probability=True)
# svclf.fit(train_set1, target_train)  
# pred_svc = svclf.predict(test_set1)
# print('SVM=',sum(pred_svc==target_test)/len(target_test))


from sklearn.naive_bayes import GaussianNB
nbclf = GaussianNB()
nbclf.fit(train_set1, target_train)  
pred_nb = nbclf.predict(test_set1);
print('NB=',sum(pred_nb==target_test)/len(target_test))

time_end=time.time()
print('time cost',time_end-time_start,'s')
