#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

from keras.datasets import imdb
from keras.layers import Dense, Embedding, SimpleRNN
from keras.models import Sequential
from keras.preprocessing import sequence

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # or any {'0', '1', '2'}

vocabulary = 10000  # 只用词典使用频率前10000的单词
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=vocabulary)

# 构建字典 key为id value为单词 +3是因为0、1、2是保留的
id_to_word = {id_ + 3: word for word, id_ in imdb.get_word_index().items()}

# 0表示填充令牌"<pad>" 1表示序列开始"<sos>" 2表示未知单词"<unk>"
for id_, token in enumerate(("<pad>", "<sos>", "<unk>")):
    id_to_word[id_] = token

# 显示前5条评论的前10个单词的id表示和原文
for i in range(5):
    print(X_train[i][:10])
    print(" ".join([id_to_word[id_] for id_ in X_train[i][:10]]))

# 每条评论截断或补齐为相同长度
X_train = sequence.pad_sequences(X_train, maxlen=500)
X_test = sequence.pad_sequences(X_test, maxlen=500)

model = Sequential()
model.add(Embedding(vocabulary, 32))
model.add(SimpleRNN(32))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics='acc')
model.summary()

model.fit(X_train, y_train, epochs=3, batch_size=128)

model.evaluate(X_test, y_test, verbose=2)
