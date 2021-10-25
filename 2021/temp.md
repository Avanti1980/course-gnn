---
presentation:
  transition: "none"
  enableSpeakerNotes: true
  margin: 0
---

@import "../common/css/font-awesome-4.7.0/css/font-awesome.css"
@import "../common/css/zhangt-solarized.css"
@import "css/GNN.css"

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 卷积神经网络

```python
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras import Sequential
from tensorflow.keras.datasets.mnist import load_data
from tensorflow.keras.layers import (Conv2D, Dense, Dropout, Flatten, MaxPool2D)
from tensorflow.keras.optimizers import Adam

print(tf.__version__)
print(tf.keras.__version__)
--------
2.6.0
2.6.0

(x_train, y_train), (x_test, y_test) = load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
print(x_train.shape)
print(x_test.shape)
--------
(60000, 28, 28)
(10000, 28, 28)

x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)
print(x_train.shape)
print(x_test.shape)
--------
(60000, 28, 28, 1)
(10000, 28, 28, 1)

model = Sequential()
model.add(Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)))
model.add(MaxPool2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation="relu"))
model.add(MaxPool2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation="relu"))
model.add(Flatten())
model.add(Dense(64, activation="relu"))
model.add(Dense(10, activation="softmax"))
model.compile(
    optimizer=Adam(0.001),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test, verbose=2)
--------
Epoch 1/5
1875/1875 [=================] - 6s 2ms/step - loss: 0.1480 - accuracy: 0.9534
Epoch 2/5
1875/1875 [=================] - 4s 2ms/step - loss: 0.0457 - accuracy: 0.9856
Epoch 3/5
1875/1875 [=================] - 4s 2ms/step - loss: 0.0330 - accuracy: 0.9899
Epoch 4/5
1875/1875 [=================] - 4s 2ms/step - loss: 0.0248 - accuracy: 0.9923
Epoch 5/5
1875/1875 [=================] - 4s 2ms/step - loss: 0.0195 - accuracy: 0.9939

313/313 - 0s - loss: 0.0264 - accuracy: 0.9923
```

GNN-FOOTER 图神经网络导论 卷积神经网络 tengzhang@hust.edu.cn
