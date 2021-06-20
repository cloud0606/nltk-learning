from gensim.corpora import WikiCorpus
import zhconv
import jieba
def fmt2txt():
    # 格式转为 txt
    print('start')
    input_file_name = './zhwiki-latest-pages-articles.xml.bz2'
    output_file_name = 'wiki.cn.txt'
    print('reading')
    input_file = WikiCorpus(input_file_name, dictionary={})
    print('read finished')
    output_file = open(output_file_name, 'w', encoding="utf-8")
    count = 0
    for text in input_file.get_texts():
        output_file.write(' '.join(text) + '\n')
        count = count + 1
        if count % 10000 == 0:
            print('num %d' % count)
    output_file.close()
    print('Finished')

def convert_fmt_jieba():
    print('start cut ')
    count = 0
    fin = open('./wiki.cn.txt', 'r', encoding='utf-8')
    fout = open('./wwiki.cn.simple.separate.txt', 'w', encoding='utf-8')
    for line in fin.readlines():
        count += 1
        # print('-'*30)
        # print(line)
        line_simp = zhconv.convert(line, 'zh-hans')
        # print(line_simp)
        # print(' '.join(jieba.cut(line_simp.split('\n')[0].replace(' ', ''))) + '\n')
        fout.write(' '.join(jieba.cut(line_simp.split('\n')[0].replace(' ', ''))) + '\n')
        if count % 10000 == 0:
            print('目前已分词%d条数据' % count)
    fin.close()
    fout.close()

if __name__ == '__main__':
    # fmt2txt()
    convert_fmt_jieba()
    print('hi')