@import "common/css/font-awesome-4.7.0/css/font-awesome.css"
@import "common/css/index.css"

## 图神经网络导论 2021

---

#### 概况

授课：张腾、32 学时

- 前 24 学时：理论知识，周三、周五上午 1-2 节课，西十二 S404
- 后 8 学时：动手实践，周五下午 5-8 节课

#### 考核

一份课堂报告，一份实验报告

#### 课件

在线浏览，Space 翻页，Esc 导航，校外访问或需借助科学上网

<div class="threelines outline" markdown=1>

|        |             讲义             | 内容                                                      |
| :----: | :--------------------------: | :-------------------------------------------------------- |
| 第壹讲 |     [绪论](2021/01.html)     | 1. 如何将数据表示成图，常见图的类型                       |
|   ^    |              ^               | 2. 图数据上的四类学习任务：点、边、子图、整图             |
|   ^    |              ^               | 3. 用神经网络来学习图数据有何优势                         |
|   ^    |              ^               | 4. 图神经网络的前沿研究方向                               |
| 第贰讲 | [机器学习 上](2021/02.html)  | 1. 人工智能的三次浪潮：推理期、知识期、学习期             |
|   ^    |              ^               | 2. 机器学习的基本流程：特征工程、模型学习                 |
|   ^    |              ^               | 3. 特征提取，文本数据的 tf - idf 特征                     |
|   ^    |              ^               | 4. 特征处理：离散类别特征、缺失特征、标准化               |
|   ^    |              ^               | 5. 特征选择：方差分析、卡方检验、互信息、稀疏范数         |
|   ^    |              ^               | 6. 特征变换：PCA、随机投影、核方法、非线性复合            |
| 第叁讲 | [机器学习 下](2021/03.html)  | 1. 监督学习、半监督学习、无监督学习及其各自代表性任务     |
|   ^    |              ^               | 2. 泛化风险，经验风险，过拟合，VC 维，宽打散维            |
|   ^    |              ^               | 3. 结构风险最小化，大间隔准则，正则化，替代损失           |
|   ^    |              ^               | 4. 一阶优化算法：梯度下降，随机梯度下降，加速梯度下降     |
|   ^    |              ^               | 5. 回归模型：线性回归，岭回归，LASSO，支持向量回归        |
|   ^    |              ^               | 6. 分类模型：感知机，支持向量机，对数几率回归，神经网络   |
| 第肆讲 |   [神经网络](2021/04.html)   | 1. 神经网络发展史，神经元和神经网络的基本概念和形式化     |
|   ^    |              ^               | 2. 激活函数：Sigmoid 型、ReLU 族、Swish 函数、Maxout 单元 |
|   ^    |              ^               | 3. 反向传播 (BP) 算法的推导，梯度消失，残差网络           |
|   ^    |              ^               | 4. 优化算法：步长衰减、步长预热、周期性步长、自适应步长   |
|   ^    |              ^               | 5. 训练技巧：初始化、归一化、超参数选择、dropout、mixup   |
| 第伍讲 | [卷积神经网络](2021/05.html) | 1. 针对网格型数据，局部连接、权值共享，降低模型复杂度     |
|   ^    |              ^               | 2. 二维卷积即图像滤波，学习卷积核即学习有效的滤波方式     |
|   ^    |              ^               | 3. 窄、宽、等宽卷积，长度、步长、补零，微步、空洞卷积     |
|   ^    |              ^               | 4. 经典网络结构：LeNet-5、AlexNet、Inception、GoogLeNet   |
| 第陆讲 | [循环神经网络](2021/06.html) | 1. 针对序列型数据，带有环路，网络具有短期记忆能力         |
|   ^    |              ^               | 2. 三种模式：序列到类，同步的序列到序列，编码器-解码器    |
|   ^    |              ^               | 3. 长程依赖问题：LSTM 网络，GRU 网络，深层循环网络        |
|   ^    |              ^               | 4. 注意力机制：键值对注意力，多头注意力，自注意力         |
| 第柒讲 |  [图神经网络](2021/08.html)  | 1. 神经消息传递框架：GNN 的统一表示形式                   |
|   ^    |              ^               | 2. GNN 的衍生变种：汇聚操作的修改、更新操作的修改         |
|   ^    |              ^               | 3. 应用于加权图、异构图、二部图、动态图、超图的 GNN       |
|   ^    |              ^               | 4. 应用于点层面任务、(子) 图层面任务、边层面任务的 GNN    |

</div>

#### 参考资料

[矩阵求导](2021/supp-matrix-calculus.html)

#### 代码

第贰讲：

- [文本特征提取](python/text-feat.ipynb)、[独热编码](python/one-hot-encoding.ipynb)、[缺失特征处理](python/missing-feat.ipynb)、[特征标准化](python/feat-scaler.ipynb)、[特征选择](python/feat-selection.ipynb)
- [稀疏范数](python/sparse-norm.ipynb)、[PCA](python/pca.ipynb)、[随机投影](python/random-projection.ipynb)

<br>

第叁讲：

- [二分类示例](python/binary-classif.ipynb)、[多分类示例](python/multi-classif.ipynb)
- [k 均值聚类](python/clustering.ipynb)、[密度估计](python/density-estimation.ipynb)
- [梯度下降](python/gradient-descent.ipynb)、[动量法](python/momentum.ipynb)

<br>

第肆讲：[用 tensorflow 实现全连接网络学习乳腺癌数据](python/dnn-wdbc.py)

<br>

第伍讲：

- [用 tensorflow 实现 LeNet-5 识别 mnist 手写数字](python/lenet5-mnist.py)
- [用预训练的 Resnet50 预测图片类别](python/resnet50.py)
- [提取预训练的 VGG16 最后一个卷积层的特征](python/vgg16.py)
- [提取预训练的 VGG19 任意一层的特征](python/vgg19.py)
- [在自己的数据上微调预训练好的 Inception V3](python/vgg19.py)

第陆讲：[用 tensorflow 实现简单循环网络做 IMDB 情感分析](python/rnn4imdb.py)
