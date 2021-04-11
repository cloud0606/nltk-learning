from nltk.corpus import movie_reviews
import random
import nltk
from nltk.corpus import stopwords
import time 
import matplotlib.pyplot as plt


def gettu(fd1):
	'提取分类效果最好的词，并绘制分类效果-词频曲线。'
	fp = open("most_informative_features.txt",'r')
	w_lis = []
	e_lis = []
	f_lis = []
	for line in fp.readlines():
		word, eff = line.split(":")
		w_lis.append(word)
		e_lis.append(eff)
		f_lis.append(fd1[word])
	print(e_lis, f_lis)
	plt.plot(e_lis, f_lis)
	plt.show()


def document_features(document, word_features):
	'特征提取器，标定该影评是否有特征词'	
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features


def movie_review_nb(wordRange):
	'基于NLTK实现影评NaiveBayes分类器，wordRange 为词表范围'
	# 读取数据
	time_start=time.time()
	documents = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]  #转化为词列表的影评，与标签，组成二元组 #数据集的内容格式：[[……'just', 'what', 'a', 'summer'], 'pos')] （字段，分类）
	# 选取用于构建特征的前 2000 高频词
	all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())	 #建立全部影评的词频表
	# gettu(all_words)
	all_words = all_words.most_common(wordRange)			#词频表按频率排序, 取特征词为词频表中前2000词
	word_features = [w for (w,f) in all_words]
	# en_sw = stopwords.words(fileids='english')
	# word_features= [w for w in word_features if not w in en_sw] # 不将停词算入特征
	# 数据集转为特征集
	random.shuffle(documents)
	featuresets = [(document_features(d, word_features), c) for (d,c) in documents]  # 特征提取器提取的特征结构：{……'contains(giving)': False, 'contains(ugly)': False, 'contains(manner)': False, 'contains(bloody)': False}
	# 特征集划分为训练集和测试集
	train_set, test_set = featuresets[:int(wordRange/2)], featuresets[int(wordRange/2):]
	# 训练
	classifier = nltk.NaiveBayesClassifier.train(train_set)
	# 评估分类器：
	print(nltk.classify.accuracy(classifier, test_set))
	# 观察分类特征的贡献：
	classifier.show_most_informative_features(100)
	# print(classifier.most_informative_features())
	time_end=time.time()
	print('time cost',time_end-time_start,'s')
	



movie_review_nb(2000)
# for i in range(4001)[::500]:
# 	if i == 0:
# 		continue
# 	print(i)
# 	movie_review_nb(i)
