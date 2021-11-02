#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.datasets.mnist import load_data
from tensorflow.keras.layers import (Conv2D, Dense, Dropout,
                                     Flatten, AveragePooling2D)
from tensorflow.keras.optimizers import Adam

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # or any {'0', '1', '2'}

print(tf.__version__)
print(tf.keras.__version__)

gpus = tf.config.experimental.list_physical_devices("GPU")
if gpus:
    try:  # Currently, memory growth needs to be the same across GPUs
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        logical_gpus = tf.config.experimental.list_logical_devices("GPU")
        print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
    except RuntimeError as e:  # Memory growth must be set before GPUs have been initialized
        print(e)

# Download https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz to ~/.keras/datasets/mnist.npz
(x_train, y_train), (x_test, y_test) = load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

model = Sequential()
model.add(Conv2D(6, (5, 5), activation="relu",
                 padding="same", input_shape=(28, 28, 1)))
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
