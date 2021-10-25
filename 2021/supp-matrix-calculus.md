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
<div class="header"><img class="hust"></div>

<div class="bottom15"></div>

# 图神经网络导论

<hr class="width50">

## 矩阵求导

<div class="bottom5"></div>

### 计算机科学与技术学院 &nbsp; &nbsp; 张腾

<br>

#### tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 机器学习中的矩阵求导

监督学习中用梯度下降法求解 **正则化项 + 损失函数** 形式的问题

$$
\begin{align*}
    \wv ~ \leftarrow ~ \wv - \eta ~ \class{blue}{\frac{\partial F}{\partial \wv}}, ~ \Wv ~ \leftarrow ~ \Wv - \eta ~ \class{blue}{\frac{\partial F}{\partial \Wv}}
\end{align*}
$$

如何求$\partial F / \partial \wv$和$\partial F / \partial \Wv$？

<div class="bottom4"></div>

无监督学习中用极大似然法估计数据的分布，设$\Rbb^d \ni \xv \overset{\mathrm{IID}}{\sim} \Ncal (\xv | \muv, \Sigmav)$

$$
\begin{align*}
    \max_{\muv, \Sigmav} \prod_{i \in [m]} \frac{1}{(2 \pi)^{d/2}} \frac{1}{|\Sigmav|^{1/2}} \exp \left( -\frac{1}{2} (\xv_i - \muv)^\top \Sigmav^{-1} (\xv_i - \muv) \right)
\end{align*}
$$

如何求$\partial \ln |\Sigmav| / \partial \Sigmav$和$\partial \xv^\top \Sigmav^{-1} \xv / \partial \Sigmav$？

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide data-notes="" -->

GNN-HEADER 9 种求导情形

<div class="fullborder column1-bold column2-bold column3-bold">

| <span class="blue">$\partial$标量 / $\partial$标量</span> |             $\partial$标量 / $\partial$向量              |             $\partial$标量 / $\partial$矩阵              |
| :-------------------------------------------------------: | :------------------------------------------------------: | :------------------------------------------------------: |
|              $\partial$向量 / $\partial$标量              |             $\partial$向量 / $\partial$向量              | <span class="red">$\partial$向量 / $\partial$矩阵</span> |
|              $\partial$矩阵 / $\partial$标量              | <span class="red">$\partial$矩阵 / $\partial$向量</span> | <span class="red">$\partial$矩阵 / $\partial$矩阵</span> |

</div>

<span class="blue">$\partial$标量 / $\partial$标量</span>就是我们熟悉的单变量求导

<span class="red">$\partial$向量 / $\partial$矩阵、$\partial$矩阵 / $\partial$向量、$\partial$矩阵 / $\partial$矩阵</span>会涉及高阶张量

我们考虑剩下的 5 种情形

- $\partial$标量 / $\partial$向量
- $\partial$标量 / $\partial$矩阵
- $\partial$向量 / $\partial$标量
- $\partial$矩阵 / $\partial$标量
- $\partial$向量 / $\partial$向量

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 矩阵求导的分子布局

设$\xv \in \Rbb^l$，$\Xv \in \Rbb^{m \times n}$，<span class="blue">标量对矩阵的求导结果与分母转置尺寸相同</span>

$$
\begin{align*}
    \frac{\partial u}{\partial \xv} \triangleq \begin{bmatrix} \frac{\partial u}{\partial x_1} & \ldots & \frac{\partial u}{\partial x_l} \end{bmatrix}, ~ \frac{\partial u}{\partial \Xv} \triangleq \begin{bmatrix}
        \frac{\partial u}{\partial x_{11}} & \ldots & \frac{\partial u}{\partial x_{m1}} \\
        \vdots                                                      & \ddots & \vdots                             \\
        \frac{\partial u}{\partial x_{1n}} & \ldots & \frac{\partial u}{\partial x_{mn}}
    \end{bmatrix} \in \Rbb^{n \times m}
\end{align*}
$$

<div class="bottom4"></div>

设$\uv \in \Rbb^l$，$\Uv \in \Rbb^{m \times n}$，<span class="blue">矩阵对标量的求导结果与分子尺寸相同</span>

$$
\begin{align*}
    \frac{\partial \uv}{\partial x} \triangleq \begin{bmatrix}
        \frac{\partial u_1}{\partial x} \\ \vdots \\ \frac{\partial u_l}{\partial x}
    \end{bmatrix}, \quad
    \frac{\partial \Uv}{\partial x} \triangleq \begin{bmatrix}
        \frac{\partial u_{11}}{\partial x} & \ldots & \frac{\partial u_{1n}}{\partial x} \\
        \vdots                             & \ddots & \vdots                             \\
        \frac{\partial u_{m1}}{\partial x} & \ldots & \frac{\partial u_{mn}}{\partial x}
    \end{bmatrix} \in \Rbb^{m \times n}
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 矩阵求导的分子布局

设$\uv \in \Rbb^l$，$\xv \in \Rbb^m$，向量对向量求导的定义为 Jacobian 矩阵：

$$
\begin{align*}
    \frac{\partial \uv}{\partial \xv} \triangleq \begin{bmatrix}
        \frac{\partial u_1}{\partial x_1} & \frac{\partial u_1}{\partial x_2} & \ldots & \frac{\partial u_1}{\partial x_m} \\
        \frac{\partial u_2}{\partial x_1} & \frac{\partial u_2}{\partial x_2} & \ldots & \frac{\partial u_2}{\partial x_m} \\
        \vdots                            & \vdots                            & \ddots & \vdots                            \\
        \frac{\partial u_l}{\partial x_1} & \frac{\partial u_l}{\partial x_2} & \ldots & \frac{\partial u_l}{\partial x_m}
    \end{bmatrix}  \in \Rbb^{l \times m}
\end{align*}
$$

即<span class="blue">行数与分子尺寸相同</span>、<span class="blue">列数与分母尺寸相同</span>。

<div class="bottom4"></div>

- 分子布局的好处是链式法则跟单变量求导中的顺序一样
- 分子布局的坏处是计算梯度时要多做一个转置，因为我们更习惯梯度是列向量
- 分母布局的结果均是分子布局的转置，好处是算梯度时不用做转置，坏处是链式法则的顺序要完全反过来

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide data-notes="" -->

GNN-HEADER 基本结果

单变量求导中<span class="blue">常量的导数为零</span>：$\partial a / \partial x = 0$

类似的这里有

$$
\begin{align*}
    \frac{\partial \av}{\partial x} = \zerov, ~ \frac{\partial a}{\partial \xv} = \zerov^\top, ~ \frac{\partial \av}{\partial \xv} = \zerov, ~ \frac{\partial \Av}{\partial x} = \zerov, ~ \frac{\partial a}{\partial \Xv} = \zerov^\top
\end{align*}
$$

<div class="bottom4"></div>

单变量求导中<span class="blue">常数标量乘</span>的求导法则为$\partial (a u) / \partial x = a \cdot \partial u / \partial x$

类似的这里有

$$
\begin{align*}
    \frac{\partial a \uv}{\partial x} = a \frac{\partial \uv}{\partial x}, ~ \frac{\partial a u}{\partial \xv} = a \frac{\partial u}{\partial \xv}, ~ \frac{\partial a \uv}{\partial \xv} = a \frac{\partial \uv}{\partial \xv}, ~ \frac{\partial a \Uv}{\partial x} = a \frac{\partial \Uv}{\partial x}, ~ \frac{\partial a u}{\partial \Xv} = a \frac{\partial u}{\partial \Xv}
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 基本结果

单变量微积分中<span class="blue">乘法</span>的求导法则为$\frac{\partial uv}{\partial x} = \frac{\partial u}{\partial x} v + u \frac{\partial v}{\partial x}$

类似的这里有

$$
\begin{align*}
     & \frac{\partial \uv \vv}{\partial x} = \frac{\partial \uv}{\partial x} \vv + \uv \frac{\partial \vv}{\partial x}, \quad \frac{\partial uv}{\partial \xv} = \frac{\partial u}{\partial \xv} v + u \frac{\partial v}{\partial \xv} \\
     & \frac{\partial \Uv \Vv}{\partial x} = \frac{\partial \Uv}{\partial x} \Vv + \Uv \frac{\partial \Vv}{\partial x}, \quad \frac{\partial uv}{\partial \Xv} = \frac{\partial u}{\partial \Xv} v + u \frac{\partial v}{\partial \Xv}
\end{align*}
$$

其中第二行是因为

$$
\begin{align*}
    \left[ \frac{\partial \Uv \Vv}{\partial x} \right]_{ij} & = \frac{\partial \sum_k u_{ik} v_{kj}}{\partial x} = \sum_k \frac{\partial u_{ik}}{\partial x} v_{kj} + \sum_k u_{ik} \frac{\partial v_{kj}}{\partial x} = \left[ \frac{\partial \Uv}{\partial x} \Vv \right]_{ij} + \left[ \Uv \frac{\partial \Vv}{\partial x} \right]_{ij} \\
    \left[ \frac{\partial uv}{\partial \Xv} \right]_{ij}    & = \frac{\partial uv}{\partial x_{ji}} = \frac{\partial u}{\partial x_{ji}} v + u \frac{\partial v}{\partial x_{ji}} = \left[ \frac{\partial u}{\partial \Xv} \right]_{ij} v + u \left[ \frac{\partial v}{\partial \Xv} \right]_{ij}
\end{align*}
$$

第一行可看作第二行的特例。$\partial \uv \vv / \partial \xv$有两种可能，一是$\uv \vv$为标量，即两者的内积，这里暂且不表，后文再讲；二是$\uv \vv$为矩阵，这属于我们不考虑的$\partial 矩阵 / \partial 向量$情形。

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn
