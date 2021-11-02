#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

import numpy as np
from tensorflow.keras.applications import resnet50
from tensorflow.keras.preprocessing import image

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # or any {'0', '1', '2'}

model = resnet50.ResNet50(weights='imagenet')
model.summary()

img = image.load_img('../common/img/tj224x224.jpg', target_size=(224, 224))

# 增加通道数 RGB: (224, 224, 3) 灰度图: (224, 224, 1)
x = image.img_to_array(img)

x = np.expand_dims(x, axis=0)  # batch_size = 1
x = resnet50.preprocess_input(x)  # 中心化

preds = model.predict(x)
print(resnet50.decode_predictions(preds, top=10)[0])
