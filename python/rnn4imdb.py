#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

from keras.datasets import imdb
from keras.layers import Dense, Embedding, SimpleRNN
from keras.models import Sequential
from keras.preprocessing import sequence
from tensorflow.keras.optimizers import Adam

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # or any {'0', '1', '2'}

vocabulary = 10000

(input_train, y_train), (input_test, y_test) = imdb.load_data(num_words=vocabulary)

# 截断或补齐为相同长度
input_train = sequence.pad_sequences(input_train, maxlen=500)
input_test = sequence.pad_sequences(input_test, maxlen=500)

model = Sequential()
model.add(Embedding(vocabulary, 32))
model.add(SimpleRNN(32))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer=Adam(0.001),
              loss='binary_crossentropy',
              metrics=['acc'])
model.summary()

model.fit(input_train, y_train,
          epochs=5,
          batch_size=128,
          validation_split=0.2)

model.evaluate(input_test, y_test, verbose=2)
