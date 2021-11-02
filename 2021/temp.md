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

GNN-HEADER 经典网络复用

使用在 ImageNet 训练好的残差网络 ResNet50 进行图像分类

```python {.line-numbers}
import numpy as np
from tensorflow.keras.applications import resnet50
from tensorflow.keras.preprocessing import image

model = resnet50.ResNet50(weights='imagenet')
img = image.load_img('../common/img/tj224x224.jpg', target_size=(224,224))

# RGB: (224,224) → (224, 224, 3) 灰度图: (224,224) → (224, 224, 1)
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)  # batch_size = 1
x = resnet50.preprocess_input(x)  # 中心化
preds = model.predict(x)
resnet50.decode_predictions(preds, top=5)[0]

('n03630383', 'lab_coat', 0.24623604),     实验服
('n03877472', 'pajama', 0.17045474),       睡衣
('n04317175', 'stethoscope', 0.095500074), 听诊器
('n04479046', 'trench_coat', 0.07988542),  军用雨衣
('n03617480', 'kimono', 0.055965725),      和服
```

<img src="../common/img/tj.jpg" style="height:250px;width:250px;margin-left:auto;margin-right:2.5rem;margin-top:-26%">

GNN-FOOTER 图神经网络导论 卷积神经网络 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="从这个例子也可以看出全连接层的参数量巨大，fc1超过1亿参数，总网络不到1亿4千万" -->

GNN-HEADER 经典网络复用

使用 VGG16 提取特征

```python {.line-numbers}
import numpy as np
from tensorflow.keras.applications import vgg16
from tensorflow.keras.preprocessing import image

vgg16.VGG16(weights='imagenet').summary()
model = vgg16.VGG16(weights='imagenet', include_top=False)

img = image.load_img('../common/img/tj224x224.jpg', target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)  # batch_size = 1
x = vgg16.preprocess_input(x)  # 中心化

feat = model.predict(x)
feat.shape

Model: "vgg16"
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
input_1 (InputLayer)         [(None, 224, 224, 3)]     0
_________________________________________________________________
......
_________________________________________________________________
block5_conv3 (Conv2D)        (None, 14, 14, 512)       2359808
_________________________________________________________________
block5_pool (MaxPooling2D)   (None, 7, 7, 512)         0
_________________________________________________________________
flatten (Flatten)            (None, 25088)             0
_________________________________________________________________
fc1 (Dense)                  (None, 4096)              102764544
_________________________________________________________________
fc2 (Dense)                  (None, 4096)              16781312
_________________________________________________________________
predictions (Dense)          (None, 1000)              4097000
=================================================================
Total params: 138,357,544
Trainable params: 138,357,544
Non-trainable params: 0
_________________________________________________________________
(1, 7, 7, 512)
```

GNN-FOOTER 图神经网络导论 卷积神经网络 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 经典网络复用

从 VGG19 的任意中间层中抽取特征

```python {.line-numbers}
import numpy as np
from tensorflow.keras.applications import vgg19
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing import image

base_model = vgg19.VGG19(weights='imagenet')
base_model.summary()

model = Model(inputs=base_model.input,
              outputs=base_model.get_layer('block4_pool').output)

img = image.load_img('../common/img/tj224x224.jpg', target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)  # batch_size = 1
x = vgg19.preprocess_input(x)  # 中心化

feat = model.predict(x)
print(feat.shape)

Model: "vgg19"
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
input_1 (InputLayer)         [(None, 224, 224, 3)]     0
_________________________________________________________________
......
_________________________________________________________________
block4_conv4 (Conv2D)        (None, 28, 28, 512)       2359808
_________________________________________________________________
block4_pool (MaxPooling2D)   (None, 14, 14, 512)       0
_________________________________________________________________
block5_conv1 (Conv2D)        (None, 14, 14, 512)       2359808
_________________________________________________________________
block5_conv2 (Conv2D)        (None, 14, 14, 512)       2359808
_________________________________________________________________
block5_conv3 (Conv2D)        (None, 14, 14, 512)       2359808
_________________________________________________________________
block5_conv4 (Conv2D)        (None, 14, 14, 512)       2359808
_________________________________________________________________
block5_pool (MaxPooling2D)   (None, 7, 7, 512)         0
_________________________________________________________________
flatten (Flatten)            (None, 25088)             0
_________________________________________________________________
fc1 (Dense)                  (None, 4096)              102764544
_________________________________________________________________
fc2 (Dense)                  (None, 4096)              16781312
_________________________________________________________________
predictions (Dense)          (None, 1000)              4097000
=================================================================
Total params: 143,667,240
Trainable params: 143,667,240
Non-trainable params: 0
_________________________________________________________________
(1, 14, 14, 512)
```

GNN-FOOTER 图神经网络导论 卷积神经网络 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 经典网络复用

在新数据上微调 InceptionV3

```python {.line-numbers}
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model

base_model = InceptionV3(weights='imagenet', include_top=False)
for i, layer in enumerate(base_model.layers):
    print(i, layer.name)

x = base_model.output
x = GlobalAveragePooling2D()(x)  # 全局平均池化层
x = Dense(1024, activation='relu')(x)  # 全连接层
predictions = Dense(200, activation='softmax')(x)  # 输出层 假设有200个类
model = Model(inputs=base_model.input, outputs=predictions)

for layer in base_model.layers:
    layer.trainable = False  # 锁住所有InceptionV3的层

model.compile(optimizer='rmsprop', loss='categorical_crossentropy')
model.fit(...)  # 在新的数据集上训练新加层的参数

for layer in model.layers[:249]:
    layer.trainable = False  # 锁住当前网络的前250层
for layer in model.layers[249:]:
    layer.trainable = True

model.compile(optimizer='rmsprop', loss='categorical_crossentropy')
model.fit(...)

0 input_1
1 conv2d
2 batch_normalization
3 activation
4 conv2d_1
5 batch_normalization_1
6 activation_1
......
305 batch_normalization_93
306 activation_85
307 mixed9_1
308 concatenate_1
309 activation_93
310 mixed10
```

GNN-FOOTER 图神经网络导论 卷积神经网络 tengzhang@hust.edu.cn
