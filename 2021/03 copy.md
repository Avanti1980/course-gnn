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

GNN-HEADER 训练技巧

训练神经网络有很多奇技淫巧

- 参数初始化
- 逐层归一化
- 超参数选择
- 权重衰减
- 提前停止
- 随机丢弃
- 数据增强
- Mixup

GNN-FOOTER 图神经网络导论 神经网络 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 参数初始化

感知机、支持向量机、对数几率回归的$\wv$通常初始化为零

</br>

神经网络的$\Wv$如果全部初始化为零，在第一遍前向计算时，所有的隐层神经元的激活值都相同，这样会导致深层神经元没有区分性

</br>

方案：随机初始化

</br>

策略：<span class="blue">保持每个神经元输入和输出的方差一致</span>

</br>

第$l$个隐层的神经元$z$接受前一层的输出$a_1, \ldots, a_{n_{l-1}}$作为输入

$$
\begin{align*}
    z = \sum_{i \in [n_{l-1}]} w_i a_i
\end{align*}
$$

GNN-FOOTER 图神经网络导论 神经网络 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 参数初始化

假设$w_i$和$a_i$的均值都为$0$，并且互相独立，则$z$的方差为

$$
\begin{align*}
    \var[z] = \sum_{i \in [n_{l-1}]} \var[w_i] \var[a_i] = n_{l-1} \var[w_i] \var[a_i]
\end{align*}
$$

</br>

若想保持每个神经元的输入和输出的方差一致，则有$\var[w_i] = 1 / n_{l-1}$

</br>

同理在反向传播中，若想误差信号也不被放大或缩小，需将$w_i$的方差保持为$\var[w_i] = 1 / n_l$

</br>

两相折中，可以设置$\var[w_i] = 2 / (n_l + n_{l-1})$

- <span class="blue">正态分布初始化</span>，$\Ncal (0, \sqrt{2 / (n_l + n_{l-1})})$
- <span class="blue">均匀分布初始化</span>，若分布区间为$[-r,r]$，则$r = \sqrt{6 / (n_l + n_{l-1})}$

GNN-FOOTER 图神经网络导论 神经网络 tengzhang@hust.edu.cn

<!-- slide data-notes="" -->

GNN-HEADER 逐层归一化

在使用随机梯度下降来训练网络时

- 每次参数更新都会导致网络中间每一层的输入的分布发生改变
- 越深的层的输入分布会改变得越明显

如果某个神经层的输入分布发生了改变，那么其参数需要重新学习

<span class="blue">批量归一化</span>(Batch Normalization, BN)：逐层将各个神经元$z$归一化到标准正态分布

$$
\begin{align*}
    \hat{z} = \frac{z - \Ebb[z]}{\sqrt{\var [z] + \epsilon}}
\end{align*}
$$

$z$的期望和方差通常用当前小批量样本集的均值和方差近似估计

批量归一化操作可以看作一个特殊的层，加在每一层非线性激活函数前：$\av_{l+1} = h(\mathrm{BN} (\Wv \av_l))$

GNN-FOOTER 图神经网络导论 神经网络 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 逐层归一化

批量归一化：针对单个神经元

- 要求小批量样本数不能太小，否则难以得到单个神经元较准确的统计信息

层归一化：针对一层的所有神经元

</br>

设小批量样本数为$k$，该层神经元数为$n$

$$
\begin{align*}
    \begin{bmatrix}
        z_{11} & z_{12} & \cdots & z_{1n} \\
        z_{21} & z_{22} & \cdots & z_{2n} \\
        \vdots & \vdots & \ddots & \vdots \\
        z_{k1} & z_{k2} & \cdots & z_{kn} \\
    \end{bmatrix}
\end{align*}
$$

</br>

- 批量归一化：对列做归一化
- 层归一化：对行做归一化，用于小批量样本数较小的时候

GNN-FOOTER 图神经网络导论 神经网络 tengzhang@hust.edu.cn

<!-- slide data-notes="" -->

GNN-HEADER 超参数选择

超参数对神经网络的性能影响很大，常见的超参数有

- 网络结构：神经元之间的连接关系、层数、每层的神经元数量、激活函数类型
- 优化参数：优化方法、步长、小批量样本数
- 正则化系数

</br>

超参数优化很难

- 组合优化问题，无法像一般参数那样通过梯度下降方法来优化，也没有一种通用有效的优化方法
- 评估一组超参数配置的时间代价非常高，从而导致一些黑盒优化方法，如演化算法难以应用

GNN-FOOTER 图神经网络导论 神经网络 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 网格搜索

尝试所有的超参数组合来寻找一组合适的超参数配置

</br>

设共有$K$个超参数，第$k$个超参数可以取$n_k$个值，那么组合总数为

$$
\begin{align*}
    n_1 \times n_2 \times \cdots \times n_K
\end{align*}
$$

</br>

如果超参数是连续的，可以将超参数离散化，选择几个“经验”值，比如正则化系数$\lambda$，可以设置

$$
\begin{align*}
    \lambda \in \{ 0.01, 0.1, 1, 10, 100 \}
\end{align*}
$$

</br>

对于连续的超参数，不能简单地按等间隔的方式离散化，需要根据超参数自身的特点进行离散化

GNN-FOOTER 图神经网络导论 神经网络 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 随机搜索

不同超参数对模型性能的影响有很大差异

</br>

有些超参数对模型性能的影响有限，例如正则化系数；而有些超参数对模型性能影响比较大，例如步长

</br>

<span class="blue">采用网格搜索会在不重要的超参数上进行不必要的尝试</span>

</br>

随机搜索：对超参数进行随机组合，然后选取一个性能最好的配置

</br>

优点：在实践中更容易实现，一般会比网格搜索更加有效

</br>

缺点：与网格搜索一样，没有利用不同超参数组合之间的相关性，即如果超参数组合比较类似，模型性能也会比较接近，因此这两种搜索方式一般都比较低效

GNN-FOOTER 图神经网络导论 神经网络 tengzhang@hust.edu.cn
