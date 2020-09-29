#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

data, label = make_blobs(n_samples=200, centers=2, random_state=0, cluster_std=0.6)
plt.scatter(data[:, 0], data[:, 1], c=label, s=50, cmap="autumn")

svm = SVC(kernel="linear")
svm.fit(data, label)

lr = LogisticRegression()
lr.fit(data, label)

ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

x = np.linspace(xlim[0], xlim[1], 50)
y = np.linspace(ylim[0], ylim[1], 50)
X, Y = np.meshgrid(x, y)
xy = np.vstack([X.ravel(), Y.ravel()]).T

V = svm.decision_function(xy).reshape(X.shape)
probs = lr.predict_proba(xy)[:, 1].reshape(X.shape)

ax.contour(X, Y, V, colors="k", levels=[-1, 0, 1], alpha=0.5, linestyles=["--"])
ax.contour(X, Y, probs, colors="k", levels=[0.5], alpha=0.5, linestyles=["-"])

plt.show()
