#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # or any {'0', '1', '2'}

import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import SGD, Adam
from tensorflow.keras.regularizers import L2

data, label = make_blobs(n_samples=5000, centers=2, random_state=0, cluster_std=0.6)
plt.scatter(data[:, 0], data[:, 1], c=label, s=50, cmap="autumn")

lr_skl = LogisticRegression()
lr_skl.fit(data, label)

lr_tf = Sequential()
lr_tf.add(
    Dense(
        1,
        use_bias=True,
        bias_initializer="zeros",
        activation="sigmoid",
        input_dim=data.shape[1],
        kernel_regularizer=L2(0.01),
    )
)
lr_tf.compile(optimizer=Adam(0.005), loss="binary_crossentropy")
lr_tf.fit(data, label, epochs=40, batch_size=32)

ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

x = np.linspace(xlim[0], xlim[1], 50)
y = np.linspace(ylim[0], ylim[1], 50)
X, Y = np.meshgrid(x, y)
xy = np.vstack([X.ravel(), Y.ravel()]).T

prob_skl = lr_skl.predict_proba(xy)[:, 1].reshape(X.shape)
ax.contour(X, Y, prob_skl, colors="k", levels=[0.5], alpha=0.5, linestyles=["-"])
prob_tf = lr_tf.predict(xy).reshape(X.shape)
ax.contour(X, Y, prob_tf, colors="k", levels=[0.5], alpha=0.5, linestyles=["--"])

plt.show()
