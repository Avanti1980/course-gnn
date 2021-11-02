---
presentation:
  transition: "none"
  enableSpeakerNotes: true
  margin: 0
---

@import "../common/css/font-awesome-4.7.0/css/font-awesome.css"
@import "../common/css/zhangt-solarized.css"
@import "css/GNN.css"

<!-- slide data-notes="第一个现代卷积网络模型" -->

GNN-HEADER 经典网络 LeNet-5

<img src="../tikz/lenet.svg" class="center width75 top1 bottom0">

```python {.line-numbers}
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 28, 28, 6)         156       
_________________________________________________________________
average_pooling2d (AveragePo (None, 14, 14, 6)         0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 10, 10, 16)        2416      
_________________________________________________________________
average_pooling2d_1 (Average (None, 5, 5, 16)          0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 1, 1, 120)         48120     
_________________________________________________________________
flatten (Flatten)            (None, 120)               0         
_________________________________________________________________
dense (Dense)                (None, 84)                10164     
_________________________________________________________________
dense_1 (Dense)              (None, 10)                850       
=================================================================
Total params: 61,706
Trainable params: 61,706
Non-trainable params: 0
```

GNN-FOOTER 图神经网络导论 卷积神经网络 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 经典网络 LeNet-5

```python {.line-numbers}
import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.datasets.mnist import load_data
from tensorflow.keras.layers import (Conv2D, Dense, Dropout,
                                     Flatten, AveragePooling2D)
from tensorflow.keras.optimizers import Adam

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
model.compile(
    optimizer=Adam(0.001),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test, verbose=2)

Epoch 1/5
1875/1875 [=============] - 5s 2ms/step - loss: 0.2169 - accuracy: 0.9316
Epoch 2/5
1875/1875 [=============] - 3s 1ms/step - loss: 0.0733 - accuracy: 0.9773
Epoch 3/5
1875/1875 [=============] - 3s 1ms/step - loss: 0.0525 - accuracy: 0.9833
Epoch 4/5
1875/1875 [=============] - 3s 1ms/step - loss: 0.0417 - accuracy: 0.9869
Epoch 5/5
1875/1875 [=============] - 3s 1ms/step - loss: 0.0330 - accuracy: 0.9898

313/313 - 0s - loss: 0.0322 - accuracy: 0.9905
```

GNN-FOOTER 图神经网络导论 卷积神经网络 tengzhang@hust.edu.cn

