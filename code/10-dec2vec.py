# -*- coding: utf-8 -*-
 
import gensim.models as g
from gensim.corpora import WikiCorpus
import logging
import zhconv
 
 
# enable logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
 
docvec_size = 192
 
 
class TaggedWikiDocument(object):
    def __init__(self, wiki):
        self.wiki = wiki
        self.wiki.metadata = True
 
    def __iter__(self):
        import jieba
        for content, (page_id, title) in self.wiki.get_texts():
            yield g.doc2vec.TaggedDocument(content, title)
 
 
def my_function():
    zhwiki_name = './zhwiki-latest-pages-articles.xml.bz2'
    wiki = WikiCorpus(zhwiki_name,  dictionary={})
    documents = TaggedWikiDocument(wiki)
 
    model = g.Doc2Vec(documents, dm=0, dbow_words=1, vector_size=docvec_size, window=8, min_count=19, workers=8)
    model.save('./wiki.doc2vec.model')
 
 
if __name__ == '__main__':
    my_function()
