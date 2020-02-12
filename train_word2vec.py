#!/usr/bin/env python                                                                                                                                                                  
# -*- coding: utf-8 -*-
#使用gensim word2vec训练脚本获取词向量


import warnings
warnings.filterwarnings(action = 'ignore', category = UserWarning, module = 'gensim')#忽略警告

import logging
import os.path
import sys
import multiprocessing

from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence,PathLineSentences
import gensim
import tkitFile

ff=tkitFile.File()

#program = os.path.basename(sys.argv[0])
#logger = logging.getLogger(program)

#logging.basicConfig(format = '%(asctime)s: %(levelname)s:' %('message)s'),level = logging.INFO)
#logger.info("running %s" % ' '.join(sys.argv))

fdir = 'model/'
ddir='data/train/'
ff.mkdir("model/")
ff.mkdir("data")
ff.mkdir("data/train")
inp = ddir + 'data_seg.txt'
outp1 = fdir + 'word2vec.model'
outp2 = fdir + 'word2vec.vector'


if os.path.isfile(outp1):
    print("增量训练")
    # 进行增量训练
    model = Word2Vec.load(outp1)
    # model.build_vocab(LineSentence(inp),update=True)
    model.build_vocab(PathLineSentences(ddir),update=True)
    # trainedWordCount = model.train(LineSentence(inp), total_examples=model.corpus_count, epochs=model.iter)
    trainedWordCount = model.train(PathLineSentences(ddir), total_examples=model.corpus_count, epochs=model.iter)
    print('更新词典: ' + str(trainedWordCount))

else:
    print("新模型")
    #model = Word2Vec(LineSentence(inp), size = 400, window = 5, min_count = 5, workers = multiprocessing.cpu_count())
    # model = Word2Vec(LineSentence(inp), size = 256, window = 5, min_count = 5,sg=1, hs=1, iter=10, workers=25)
    model = Word2Vec(PathLineSentences(ddir), size = 256, window = 5, min_count = 5,sg=1, hs=1, iter=10, workers=25)

print("保存模型")
model.save(outp1)
model.wv.save_word2vec_format(outp2, binary=False)



