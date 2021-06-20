import gensim
import re
import jieba
import numpy as np
import pandas
def segment(doc: str):
    # 停用词
    # stop_words = pd.read_csv("./data/stopwords_TUH.txt", index_col=False, quoting=3,
    #                          names=['stopword'],
    #                          sep="\n",
    #                          encoding='utf-8')
    # stop_words = list(stop_words.stopword)
	# 去掉html标签数字等
    reg_html = re.compile(r'<[^>]+>', re.S)
    doc = reg_html.sub('', doc)
    doc = re.sub('[０-９]', '', doc)
    doc = re.sub('\s', '', doc)
    word_list = list(jieba.cut(doc))
    out_str = ''
    for word in word_list:
        # if word not in stop_words:
        out_str += word
        out_str += ' '
    segments = out_str.split(sep=" ")

    return segments

def sent2vec(model, words):
    vect_list = []
    for w in words:
        try:
            vect_list.append(model.wv[w])
        except:
            continue
    vect_list = np.array(vect_list)
    vect = vect_list.sum(axis=0)
    return vect / np.sqrt((vect ** 2).sum())

def similarity(a_vect, b_vect):
    dot_val = 0.0
    a_norm = 0.0
    b_norm = 0.0
    cos = None
    for a, b in zip(a_vect, b_vect):
        dot_val += a*b
        a_norm += a**2
        b_norm += b**2
    if a_norm == 0.0 or b_norm == 0.0:
        cos = -1
    else:
        cos = dot_val / ((a_norm*b_norm)**0.5)

    return cos

def test_model():
    print("load model")
    model = gensim.models.Doc2Vec.load('./wiki.word2vec.model')
    fname1 = './sougou/C000008/10.txt'
    fname2 = './sougou/C000008/10.txt'

    st1 = open(fname1, 'r').read()
    st2 = open(fname2, 'r').read()
    print(fname1, fname2)
    # 分词
    print("segment")
    st1 = segment(st1)
    st2 = segment(st2)
    # 转成句子向量
    vect1 = sent2vec(model, st1)
    vect2 = sent2vec(model, st2)
    
    # 查看变量占用空间大小
    import sys
    print(sys.getsizeof(vect1))
    print(sys.getsizeof(vect2))

    cos = similarity(vect1, vect2)
    print("相似度：{:.4f}".format(cos))

test_model()