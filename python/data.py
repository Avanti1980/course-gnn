import os
import random

import h5py
import numpy as np
from scipy import io, sparse
from sklearn import datasets, preprocessing
import matplotlib.pyplot as plt

dataset = [['banana', 1]]  # ['diabetes_numeric', 2], ['Dorothea', 1] 读取有bug

# X, y = fetch_openml(name='parity5', version=1, return_X_y=True, data_home="../")

le = preprocessing.LabelEncoder()

for name, ver in dataset:

    print(name, ver)

    X, y = datasets.fetch_openml(name=name, version=ver, return_X_y=True)

    X = np.array(X)

    m, d = X.shape

    print(m, d)

    if len(y) == m:

        # min_max_scaler = preprocessing.MinMaxScaler()
        # if sparse.issparse(X):
        #     X = min_max_scaler.fit_transform(X.todense())
        # else:
        #     X = min_max_scaler.fit_transform(X)

        y = le.fit_transform(y)

        if len(np.unique(y)) > 2:
            y[y < 0.5] = 0
            y[y > 0.5] = 1
            print("unique value of y > 2!")

        print(type(X))
        print(X[:,0].shape)
        print(X[:,1].shape)

        plt.scatter(X[:,0], X[:,1], color = 'hotpink')
        # plt.plot(Xn, 2, 'o', color='r')
        plt.show()

    else:
        print("error!")
