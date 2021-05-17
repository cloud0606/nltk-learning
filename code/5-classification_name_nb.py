from nltk.corpus import names
import random
import nltk
def gender_features0(word):
    return {'last_letter': word[-1]}

def gender_features1(word):
	return {'last_letter': word[-1],'name_len':len(word),}

def gender_features2(word):
    return {'first_letter': word[0]}

def gender_features3(word):
    return {'last2_letter': word[-2:]}

def gender_features4(word):
    return {'first2_letter': word[:2]}

def gender_features5(word):
    return {'last_letter': word[-1], 'last2_letter': word[-2:] }

def gender_features6(word):
    return {'last_letter': word[-1], 'last2_letter': word[-2:], 'name_len':len(word)}

# 取出带标签数据
names = [(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')]
random.shuffle(names)

for i in range(7):
    func_name = "gender_features%d" % (i)
    featuresets = [(eval("{0}".format(func_name))(n), g) for (n,g) in names]  # 特征提取
    train_set, test_set = featuresets[:5000], featuresets[5000:]  # 划分训练集和测试集  
    classifier=nltk.NaiveBayesClassifier.train(train_set)  # 训练
    print("{0} accuracy : {1}".format(func_name,nltk.classify.accuracy(classifier, test_set) ))
