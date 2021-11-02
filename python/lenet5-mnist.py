#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.datasets.mnist import load_data
from tensorflow.keras.layers import AveragePooling2D, Conv2D, Dense, Flatten
from tensorflow.keras.optimizers import Adam

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # or any {'0', '1', '2'}

(x_train, y_train), (x_test, y_test) = load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

model = Sequential()
model.add(Conv2D(6, (5, 5), activation="relu", padding="same", input_shape=(28, 28, 1)))
model.add(AveragePooling2D(pool_size=(2, 2)))
model.add(Conv2D(16, (5, 5), activation="relu"))
model.add(AveragePooling2D(pool_size=(2, 2)))
model.add(Conv2D(120, (5, 5), activation="relu"))
model.add(Flatten())
model.add(Dense(84, activation="relu"))
model.add(Dense(10, activation="softmax"))
model.summary()

model.compile(
    optimizer=Adam(0.001),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test, verbose=2)
