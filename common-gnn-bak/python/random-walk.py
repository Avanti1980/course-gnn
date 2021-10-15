#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

matrix = np.array(
    [
        [0, 1 / 2, 1 / 3, 1 / 2],
        [1 / 3, 0, 1 / 3, 0],
        [1 / 3, 1 / 2, 0, 1 / 2],
        [1 / 3, 0, 1 / 3, 0],
    ]
)

v = np.array([0.5, 0, 0.3, 0.2])

print(0, v)

for i in range(50):
    v = matrix.dot(v)
    print(i + 1, v)
