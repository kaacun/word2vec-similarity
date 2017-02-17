# coding: utf-8
from gensim.models import word2vec

model = word2vec.Word2Vec.load("saved.model")
# 単語間の類似度計算
print model.similarity(u"ステーキ", u"焼肉")
print model.similarity(u"ステーキ", u"サーロイン")
print model.similarity(u"ステーキ", u"野菜")
print model.similarity(u"ステーキ", u"魚")
print model.similarity(u"ステーキ", u"ナイフ")
print model.similarity(u"ステーキ", u"ガスト")
