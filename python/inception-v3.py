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
