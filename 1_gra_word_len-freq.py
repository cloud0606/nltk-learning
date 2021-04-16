from nltk.book import *
fd1 = FreqDist(text1)  # 本质上是词频的词典
vocabulary = fd1.keys()  # 不同类型词的列表
print(fd1["a"])  # 获取某个词的频率
mw1 = fd1.most_common(50)  # 前50词的列表（词形，词频）
print(mw1)
fd1.plot(100, cumulative=True)  # 绘制前100词的词频累计图
# mw1.plot() 
text4.dispersion_plot(['democracy', 'citizen', 'freedom'])  # 词分布图