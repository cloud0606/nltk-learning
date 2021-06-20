# coding:utf-8
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

def word2vec():
    print('[*] start Word2Vec')

    input_file_name = 'wiki.zh.simple.seg.txt'
    model_file_name = 'wiki.word2vec.model'

    model = Word2Vec(LineSentence(input_file_name),
                     vector_size = 400,  # 词向量长度为400
                     window = 5,
                     min_count = 5,
                     workers = multiprocessing.cpu_count())
    print('[*] finish Word2Vec')

    print('[*] saving model')
    model.save(model_file_name)
    print('[*] finished!')

def wordcld():
    from gensim.models import Word2Vec
    from wordcloud import WordCloud
    infile = 'wiki.word2vec.model'
    word2vec_model = Word2Vec.load(infile)
    word = '三里屯'
    sim_words = word2vec_model.wv.most_similar(word, topn=10)
    d = dict(sim_words)
    d[word] = 1 # 将本体词以100%相似度放进字典中
    wc = WordCloud(background_color='white', font_path='HanyiSentyScholar.ttf', repeat=True)
    wc.generate_from_frequencies(d).to_file(f'./wc.png')

def wordsimi():
    from gensim.models import Word2Vec
    infile = 'wiki.word2vec.model'
    word2vec_model = Word2Vec.load(infile)
    words = ['三里屯', '酒吧街', '王府井', '前门大街', '长安街']
    similarities = list(word2vec_model.wv.similarity(words[0], word) for word in words)
    for word, similarity in zip(words, similarities):
        print(word, similarity, sep='\t')
wordcld()
# wordsimi()
