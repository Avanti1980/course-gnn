import os
import random

import h5py
import matplotlib.pyplot as plt
import numpy as np
from scipy import io, sparse
from sklearn import datasets, preprocessing, tree

X = [[1, '青绿', '蜷缩', '浊响'], [2, '乌黑', '蜷缩', '浊响'], [3, '青绿', '硬挺', '清脆'], [4, '乌黑', '蜷缩', '沉闷']]
y = ['好瓜', '好瓜', '坏瓜', '坏瓜']

X_test = [[5, '浅白', '蜷缩', '浊响']]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)
print(clf.predict(X_test))
