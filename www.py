#!/usr/bin/python                                                                                                                                                                      
# -*- encoding: utf-8 -*-
# coding:utf-8
import numpy as np
import gensim
import pandas as pd #引入它主要是为了更好的显示效果
# import jieba

model = gensim.models.word2vec.Word2Vec.load('model/word2vec.model')

def predict_proba(oword, iword):
    iword_vec = model[iword]
    oword = model.wv.vocab[oword]
    oword_l = model.syn1[oword.point].T
    dot = np.dot(iword_vec, oword_l)
    lprob = -sum(np.logaddexp(0, -dot) + oword.code*dot)
    return lprob

from collections import Counter
def keywords(s):
    s = [w for w in s if w in model]
    ws = {w:sum([predict_proba(u, w) for u in s]) for w in s}
    return Counter(ws).most_common()

f = open('test_data.txt', 'r')
w = open('result.txt', 'w')
s = f.readline()
# while s:
#     result = pd.Series(keywords(jieba.cut(s)))
#     for i in result:
#         print(i)
#         ci = i[0]
#         print(ci)
#         # print("============")
#         # w.write(ci.encode('utf-8'))
#         # w.write('   ')
#     w.write('\n')
#     s = f.readline()

s ="""

哈士奇是好狗，只是不适合作为宠物。哈士奇是工作犬，被毛厚，骨骼健壮，运动量大，性格好奇而坚毅，是雪橇犬种之一，这些是长期人工选择的结果。所以最适合它的是和小伙伴们一起，拉着主人在无垠的雪地上跑来跑去。
"""
result = pd.Series(keywords(jieba.cut(s)))
print(result[:10])


# from jieba.analyse import *
# # data = open('usercontent.txt').read()#读取文件
# for keyword,weight in textrank(s,withWeight = True ):
#     print('%s %s' %(keyword,weight))


# 计算两个词的相似度/相关程度
y1 = model.similarity(u"哈士奇", u"狗")

print(y1)
# 计算某个词的相关词列表
y2 = model.most_similar(['柯基','犬'], topn=20) # 20个最相关的
print(y2)
# 计算某个词的相关词列表
y2 = model.similar_by_word(u"柯基犬", topn=20) # 20个最相关的
print(y2)
y2 = model.n_similarity(u"柯基犬", topn=20) # 20个最相关的
print(y2)

# 寻找对应关系
print (u"书-不错，质量-")
y3 = model.most_similar([u'质量', u'不错'], [u'书'], topn=3)
for item in y3:
  print (item[0], item[1])
print ("--------\n")



# 寻找不合群的词
y4 = model.doesnt_match(u"书 书籍 教材 很".split())
print (u"不合群的词：", y4)
print ("--------\n")