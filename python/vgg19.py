#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

import numpy as np
from tensorflow.keras.applications import vgg19
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing import image

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # or any {'0', '1', '2'}

base_model = vgg19.VGG19(weights='imagenet')
base_model.summary()

model = Model(inputs=base_model.input,
              outputs=base_model.get_layer('block4_pool').output)

img = image.load_img('../common/img/tj224x224.jpg', target_size=(224, 224))

# 增加通道数 RGB: (224, 224, 3) 灰度图: (224, 224, 1)
x = image.img_to_array(img)

x = np.expand_dims(x, axis=0)  # batch_size = 1
x = vgg19.preprocess_input(x)  # 中心化

feat = model.predict(x)
print(feat.shape)
