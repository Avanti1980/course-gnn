---
presentation:
  transition: "none"
  enableSpeakerNotes: true
  margin: 0
---

@import "../common/css/font-awesome-4.7.0/css/font-awesome.css"
@import "../common/css/zhangt-solarized.css"
@import "css/GNN.css"

<!-- slide data-notes="" -->

GNN-HEADER 用 tensorflow 实现

```python {.line-numbers}
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import SGD

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

model = Sequential()
model.add(Dense(64, activation="relu"))
model.add(Dense(64, activation="relu"))
model.add(Dense(1, activation="sigmoid"))
model.compile(optimizer=SGD(0.001),
              loss="binary_crossentropy",
              metrics=["accuracy"],
              )

model.fit(X_train, y_train, epochs=10)
model.evaluate(X_test, y_test, verbose=2)

Epoch 1/10
14/14 [================] - 1s 1ms/step - loss: 51.0188 - accuracy: 0.4906
Epoch 2/10
14/14 [================] - 0s 1ms/step - loss: 1.0154 - accuracy: 0.7465
Epoch 3/10
14/14 [================] - 0s 1ms/step - loss: 0.5027 - accuracy: 0.8146
Epoch 4/10
14/14 [================] - 0s 1ms/step - loss: 0.4219 - accuracy: 0.8239
Epoch 5/10
14/14 [================] - 0s 1ms/step - loss: 0.4142 - accuracy: 0.8380
Epoch 6/10
14/14 [================] - 0s 1ms/step - loss: 0.3101 - accuracy: 0.8779
Epoch 7/10
14/14 [================] - 0s 1ms/step - loss: 0.2744 - accuracy: 0.8944
Epoch 8/10
14/14 [================] - 0s 1ms/step - loss: 0.2454 - accuracy: 0.9061
Epoch 9/10
14/14 [================] - 0s 1ms/step - loss: 0.3001 - accuracy: 0.8897
Epoch 10/10
14/14 [================] - 0s 1ms/step - loss: 0.2557 - accuracy: 0.8991

5/5 - 0s - loss: 0.2264 - accuracy: 0.9231
```

GNN-FOOTER 图神经网络导论 神经网络 tengzhang@hust.edu.cn
