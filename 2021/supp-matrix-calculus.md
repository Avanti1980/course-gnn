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
    \wv ~ \leftarrow ~ \wv - \eta ~ \class{blue}{\frac{\partial F(\wv)}{\partial \wv}}, \quad \Wv ~ \leftarrow ~ \Wv - \eta ~ \class{blue}{\frac{\partial F(\Wv)}{\partial \Wv}}
\end{align*}
$$

如何求$\partial F(\wv) / \partial \wv$和$\partial F(\Wv) / \partial \Wv$？

<div class="bottom4"></div>

无监督学习中用极大似然法估计数据的分布，设$\Rbb^d \ni \xv \overset{\mathrm{IID}}{\sim} \Ncal (\xv | \muv, \Sigmav)$

$$
\begin{align*}
    \max_{\muv, \Sigmav} \prod_{i \in [m]} \frac{1}{(2 \pi)^{d/2}} \frac{1}{|\Sigmav|^{1/2}} \exp \left( -\frac{1}{2} (\xv_i - \muv)^\top \Sigmav^{-1} (\xv_i - \muv) \right)
\end{align*}
$$

如何求$\partial \muv^\top \Sigmav^{-1} \muv / \partial \muv$、$\partial \ln |\Sigmav| / \partial \Sigmav$、$\partial \muv^\top \Sigmav^{-1} \muv / \partial \Sigmav$？

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide data-notes="" -->

GNN-HEADER 9 种求导情形

<div class="fullborder column1-bold column2-bold column3-bold">

|  <span class="blue">$\partial$标量 /$\partial$标量</span>  | <span class="yellow">$\partial$标量 /$\partial$向量</span> | <span class="yellow">$\partial$标量 /$\partial$矩阵</span> |
| :--------------------------------------------------------: | :--------------------------------------------------------: | :--------------------------------------------------------: |
| <span class="yellow">$\partial$向量 /$\partial$标量</span> | <span class="yellow">$\partial$向量 /$\partial$向量</span> |  <span class="red">$\partial$向量 /$\partial$矩阵</span>   |
| <span class="yellow">$\partial$矩阵 /$\partial$标量</span> |  <span class="red">$\partial$矩阵 /$\partial$向量</span>   |  <span class="red">$\partial$矩阵 /$\partial$矩阵</span>   |

</div>

<span class="blue">$\partial$标量 /$\partial$标量</span>就是我们熟悉的单变量求导

<span class="red">$\partial$向量 /$\partial$矩阵、$\partial$矩阵 /$\partial$向量、$\partial$矩阵 /$\partial$矩阵</span>会涉及高阶张量

我们考虑剩下的 5 种情形

- $\partial$标量 /$\partial$向量
- $\partial$标量 /$\partial$矩阵
- $\partial$向量 /$\partial$标量
- $\partial$矩阵 /$\partial$标量
- $\partial$向量 /$\partial$向量

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 矩阵求导的分子布局

<span class="blue">标量对向量、矩阵的求导结果与分母转置尺寸相同</span>

$$
\begin{align*}
    \frac{\partial u}{\partial \xv} \triangleq \begin{bmatrix} \frac{\partial u}{\partial x_1} & \ldots & \frac{\partial u}{\partial x_l} \end{bmatrix}, \quad \frac{\partial u}{\partial \Xv} \triangleq \begin{bmatrix}
        \frac{\partial u}{\partial x_{11}} & \ldots & \frac{\partial u}{\partial x_{m1}} \\
        \vdots                                                      & \ddots & \vdots                             \\
        \frac{\partial u}{\partial x_{1n}} & \ldots & \frac{\partial u}{\partial x_{mn}}
    \end{bmatrix} \in \Rbb^{n \times m}
\end{align*}
$$

<div class="bottom4"></div>

<span class="blue">向量、矩阵对标量的求导结果与分子尺寸相同</span>

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

向量对向量求导的定义为<span class="blue">雅可比矩阵</span> (行看分子、列看分母)

$$
\begin{align*}
    \frac{\partial \uv}{\partial \xv} \triangleq \begin{bmatrix}
        \frac{\partial u_1}{\partial x_1} & \frac{\partial u_1}{\partial x_2} & \ldots & \frac{\partial u_1}{\partial x_m} \\
        \frac{\partial u_2}{\partial x_1} & \frac{\partial u_2}{\partial x_2} & \ldots & \frac{\partial u_2}{\partial x_m} \\
        \vdots                            & \vdots                            & \ddots & \vdots                            \\
        \frac{\partial u_l}{\partial x_1} & \frac{\partial u_l}{\partial x_2} & \ldots & \frac{\partial u_l}{\partial x_m}
    \end{bmatrix}
    = \begin{bmatrix} \frac{\partial u_1}{\partial \xv} \\ \frac{\partial u_2}{\partial \xv} \\ \vdots \\ \frac{\partial u_l}{\partial \xv} \end{bmatrix}
    = \begin{bmatrix} \frac{\partial \uv}{\partial x_1} & \frac{\partial \uv}{\partial x_2} & \cdots & \frac{\partial \uv}{\partial x_m} \end{bmatrix}
\end{align*}
$$

<div class="bottom2"></div>

- 分子布局的好处是<span class="blue">链式法则跟单变量求导中的顺序一样</span>
- 分子布局的坏处是计算$\wv$的梯度$\partial F(\wv) / \partial \wv$时要<span class="blue">多做一个转置</span>
- 分母布局的结果均是分子布局的转置，好处是算梯度时不用做转置，坏处是链式法则的顺序要完全反过来
- 两者结合为混合布局，算梯度时不做转置，但链式法则的顺序无固定规律，需根据矩阵尺寸仔细推敲，新手建议先学分子布局，熟练老鸟可直接混合布局

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide data-notes="" -->

GNN-HEADER 基本结果

单变量求导中<span class="blue">常量的导数为零</span>：$\partial a / \partial x = 0$，类似的这里有

$$
\begin{align*}
    \frac{\partial \av}{\partial x} = \zerov, ~ \frac{\partial a}{\partial \xv} = \zerov^\top, ~ \frac{\partial \av}{\partial \xv} = \zerov, ~ \frac{\partial \Av}{\partial x} = \zerov, ~ \frac{\partial a}{\partial \Xv} = \zerov^\top
\end{align*}
$$

<div class="bottom2"></div>

单变量求导中<span class="blue">常数标量乘</span>的求导法则为$\frac{\partial (a u)}{\partial x} = a \frac{\partial u}{\partial x}$，类似的这里有

$$
\begin{align*}
    \frac{\partial a \uv}{\partial x} = a \frac{\partial \uv}{\partial x}, ~ \frac{\partial a u}{\partial \xv} = a \frac{\partial u}{\partial \xv}, ~ \frac{\partial a \uv}{\partial \xv} = a \frac{\partial \uv}{\partial \xv}, ~ \frac{\partial a \Uv}{\partial x} = a \frac{\partial \Uv}{\partial x}, ~ \frac{\partial a u}{\partial \Xv} = a \frac{\partial u}{\partial \Xv}
\end{align*}
$$

<div class="bottom2"></div>

单变量微积分中<span class="blue">加法</span>的求导法则为$\frac{\partial (u+v)}{\partial x} = \frac{\partial u}{\partial x} + \frac{\partial v}{\partial x}$，类似的这里有

$$
\begin{align*}
     & \frac{\partial (\uv + \vv)}{\partial x} = \frac{\partial \uv}{\partial x} + \frac{\partial \vv}{\partial x}, ~ \frac{\partial (u+v)}{\partial \xv} = \frac{\partial u}{\partial \xv} + \frac{\partial v}{\partial \xv}, ~ \frac{\partial (\uv + \vv)}{\partial \xv} = \frac{\partial \uv}{\partial \xv} + \frac{\partial \vv}{\partial \xv} \\
     & \frac{\partial (\Uv + \Vv)}{\partial x} = \frac{\partial \Uv}{\partial x} + \frac{\partial \Vv}{\partial x}, ~ \frac{\partial (u + v)}{\partial \Xv} = \frac{\partial u}{\partial \Xv} + \frac{\partial v}{\partial \Xv}
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="乘法求导就不是太显然的了" -->

GNN-HEADER 基本结果

单变量求导中<span class="blue">乘法</span>的求导法则为$\frac{\partial (uv)}{\partial x} = \frac{\partial u}{\partial x} v + u \frac{\partial v}{\partial x}$，类似的这里有

$$
\begin{align*}
     & \frac{\partial (\uv \vv)}{\partial x} = \frac{\partial \uv}{\partial x} \vv + \uv \frac{\partial \vv}{\partial x}, ~ \frac{\partial (uv)}{\partial \xv} = \frac{\partial u}{\partial \xv} v + u \frac{\partial v}{\partial \xv} \\
     & \frac{\partial (\Uv \Vv)}{\partial x} = \frac{\partial \Uv}{\partial x} \Vv + \Uv \frac{\partial \Vv}{\partial x}, ~ \frac{\partial (uv)}{\partial \Xv} = \frac{\partial u}{\partial \Xv} v + u \frac{\partial v}{\partial \Xv}
\end{align*}
$$

其中第一行可看作第二行的特例，第二行是因为

$$
\begin{align*}
    \left[ \frac{\partial (\Uv \Vv)}{\partial x} \right]_{ij} & = \sum_k \frac{\partial u_{ik}}{\partial x} v_{kj} + \sum_k u_{ik} \frac{\partial v_{kj}}{\partial x} = \left[ \frac{\partial \Uv}{\partial x} \Vv \right]_{ij} + \left[ \Uv \frac{\partial \Vv}{\partial x} \right]_{ij} \\
    \left[ \frac{\partial (uv)}{\partial \Xv} \right]_{ij}    & = \frac{\partial (uv)}{\partial x_{ji}} = \frac{\partial u}{\partial x_{ji}} v + u \frac{\partial v}{\partial x_{ji}} = \left[ \frac{\partial u}{\partial \Xv} \right]_{ij} v + u \left[ \frac{\partial v}{\partial \Xv} \right]_{ij}
\end{align*}
$$

$\partial (\uv^\top \vv) / \partial \xv$属于<span class="yellow">$\partial$标量 /$\partial$向量</span>的情形，后面再讲

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 基本结果

单变量求导中有$\partial x / \partial x = 1$，类似的这里有

$$
\begin{align*}
    \frac{\partial x_i}{\partial \xv} = \ev_i^\top, ~ \frac{\partial \xv}{\partial x_i} = \ev_i, ~ \frac{\partial \xv}{\partial \xv} = \Iv, ~ \frac{\partial x_{ij}}{\partial \Xv} = \Ev_{ji}, ~ \frac{\partial \Xv}{\partial x_{ij}} = \Ev_{ij}
\end{align*}
$$

其中

- $\ev_i$是第$i$个元素为$1$其余为$0$的向量
- $\Ev_{ij}$是$(i,j)$处为$1$其余为$0$的矩阵

<div class="bottom4"></div>

对神经网络第$l$层$\zv_l = \Wv_l ~ \av_{l-1} + \bv_l$，易知有

$$
\begin{align*}
    \frac{\partial \zv_l}{\partial \bv_l} = \frac{\partial \bv_l}{\partial \bv_l} = \Iv
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide data-notes="这里可以假设l=1，借此说一下分母布局会导致链式法则顺序反过来" -->

GNN-HEADER 链式法则

单变量求导中的<span class="blue">链式法则</span>为$\frac{\partial g(u)}{\partial x} = \frac{\partial g(u)}{\partial u} \frac{\partial u}{\partial x}$

情形一，只涉及向量：设$\xv \in \Rbb^n$，$\uv = \uv(\xv) \in \Rbb^m$，$\gv: \Rbb^m \mapsto \Rbb^l$，则

$$
\begin{align*}
    \underbrace{\class{blue}{\frac{\partial \gv(\uv)}{\partial \xv}}}_{l \times n} = \underbrace{\class{blue}{\frac{\partial \gv(\uv)}{\partial \uv}}}_{l \times m} \underbrace{\class{blue}{\frac{\partial \uv}{\partial \xv}}}_{m \times n}
\end{align*}
$$

这是因为

$$
\begin{align*}
    \left[ \frac{\partial \gv(\uv)}{\partial \xv} \right]_{ij} & = \frac{\partial [\gv(\uv)]_i}{\partial x_j} = \sum_{k \in [m]} \frac{\partial [\gv(\uv)]_i}{\partial u_k} \frac{\partial u_k}{\partial x_j} = \frac{\partial [\gv(\uv)]_i}{\partial \uv} \frac{\partial \uv}{\partial x_j} \\
    & = \left[ \frac{\partial \gv(\uv)}{\partial \uv} \right]_{i,:} \left[ \frac{\partial \uv}{\partial \xv} \right]_{:,j} = \left[ \frac{\partial \gv(\uv)}{\partial \uv} \frac{\partial \uv}{\partial \xv} \right]_{i,j}
\end{align*}
$$

注意若$n = m = l = 1$，就退化成了单变量的链式法则

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 链式法则

单变量求导中的<span class="blue">链式法则</span>为$\frac{\partial g(u)}{\partial x} = \frac{\partial g(u)}{\partial u} \frac{\partial u}{\partial x}$

情形二，自变量是矩阵：设$u = u(\Xv)$，$g: \Rbb \mapsto \Rbb$，则

$$
\begin{align*}
    \left[ \frac{\partial g(u)}{\partial \Xv} \right]_{ij} = \frac{\partial g(u)}{\partial u} \frac{\partial u}{\partial x_{ji}} = \frac{\partial g(u)}{\partial u} \left[ \frac{\partial u}{\partial \Xv} \right]_{ij} ~ \Longrightarrow ~ \class{blue}{\frac{\partial g(u)}{\partial \Xv} = \frac{\partial g(u)}{\partial u} \frac{\partial u}{\partial \Xv}}
\end{align*}
$$

情形三，中间变量是矩阵：设$\Uv = \Uv(x) \in \Rbb^{m \times n}$，$g: \Rbb^{m \times n} \mapsto \Rbb$，则

$$
\begin{align*}
    \class{blue}{\frac{\partial g(\Uv)}{\partial x}} & = \sum_p \sum_q \frac{\partial g(\Uv)}{\partial u_{pq}} \frac{\partial u_{pq}}{\partial x} = \sum_q \sum_p \left[ \frac{\partial g(\Uv)}{\partial \Uv} \right]_{qp} \left[ \frac{\partial \Uv}{\partial x} \right]_{pq} \\
    & = \class{blue}{\tr \left( \frac{\partial g(\Uv)}{\partial \Uv} \frac{\partial \Uv}{\partial x} \right)}
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide data-notes="" -->

GNN-HEADER 大纲

<div class="sparse">

<span class="blue">向量对标量求导</span>

标量对向量求导

向量对向量求导

矩阵对标量求导

标量对矩阵求导

</div>

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 向量对标量求导

矩阵和向量的乘积是向量，若$\Av$与$\xv$无关，易知有

$$
\begin{align*}
    \left[ \frac{\partial \Av \uv}{\partial x} \right]_{i} & = \frac{\partial [\Av \uv]_i}{\partial x} = \frac{\partial \sum_k a_{ik} u_k}{\partial x} = \sum_k a_{ik} \frac{\partial u_k}{\partial x} = \left[ \Av \frac{\partial \uv}{\partial x} \right]_i \\
    & \Longrightarrow \class{blue}{\frac{\partial \Av \uv}{\partial x} = \Av \frac{\partial \uv}{\partial x}}
\end{align*}
$$

于是

$$
\begin{align*}
    \frac{\partial \uv^\top \Av}{\partial x} = \left( \frac{\partial \Av^\top \uv}{\partial x} \right)^\top = \left( \Av^\top \frac{\partial \uv}{\partial x} \right)^\top = \left( \frac{\partial \uv}{\partial x} \right)^\top \Av = \frac{\partial \uv^\top}{\partial x} \Av
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="向量的外积也是向量" -->

GNN-HEADER 向量对标量求导

向量的外积也是向量

记$\uv = [u_1(x); u_2(x); u_3(x)]$，$\vv = [v_1(x); v_2(x); v_3(x)]$，则

$$
\begin{align*}
    \uv \times \vv = \begin{bmatrix}
        u_2 v_3 - u_3 v_2 \\ u_3 v_1 - u_1 v_3 \\ u_1 v_2 - u_2 v_1
    \end{bmatrix}
\end{align*}
$$

于是

$$
\begin{align*}
    \class{blue}{\frac{\partial (\uv \times \vv)}{\partial x}} & = \begin{bmatrix}
        \frac{\partial u_2}{\partial x} v_3 - \frac{\partial u_3}{\partial x} v_2 + u_2 \frac{\partial v_3}{\partial x} - u_3 \frac{\partial v_2}{\partial x} \\
        \frac{\partial u_3}{\partial x} v_1 - \frac{\partial u_1}{\partial x} v_3 + u_3 \frac{\partial v_1}{\partial x} - u_1 \frac{\partial v_3}{\partial x} \\
        \frac{\partial u_1}{\partial x} v_2 - \frac{\partial u_2}{\partial x} v_1 + u_1 \frac{\partial v_2}{\partial x} - u_2 \frac{\partial v_1}{\partial x} \\
    \end{bmatrix} \\
    & = \class{blue}{\frac{\partial \uv}{\partial x} \times \vv + \uv \times \frac{\partial \vv}{\partial x}}
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide data-notes="" -->

GNN-HEADER 大纲

<div class="sparse">

向量对标量求导

<span class="blue">标量对向量求导</span>

向量对向量求导

矩阵对标量求导

标量对矩阵求导

</div>

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 标量对向量求导

二次型是标量，设$\Av$与$\xv$无关，易知有

$$
\begin{align*}
    \left[ \frac{\partial \uv^\top \Av \vv}{\partial \xv} \right]_i & = \frac{\partial \sum_{j,k} u_j a_{jk} v_k}{\partial x_i} = \sum_{j,k} u_j a_{jk} \frac{\partial v_k}{\partial x_i} + \sum_{j,k} \frac{\partial u_j}{\partial x_i} a_{jk} v_k         \\
    & = \uv^\top \Av \frac{\partial \vv}{\partial x_i} + \vv^\top \Av^\top \frac{\partial \uv}{\partial x_i} = \left[ \uv^\top \Av \frac{\partial \vv}{\partial \xv} \right]_i + \left[ \vv^\top \Av^\top \frac{\partial \uv}{\partial \xv} \right]_i \\
    & \Longrightarrow \class{blue}{\frac{\partial \uv^\top \Av \vv}{\partial \xv} = \uv^\top \Av \frac{\partial \vv}{\partial \xv} + \vv^\top \Av^\top \frac{\partial \uv}{\partial \xv}} \\
    & \overset{\Av = \Iv}{\Longrightarrow} \frac{\partial \uv^\top \vv}{\partial \xv} = \uv^\top \frac{\partial \vv}{\partial \xv} + \vv^\top \frac{\partial \uv}{\partial \xv}
\end{align*}
$$

进一步若$\uv = \av$与$\xv$无关，则

$$
\begin{align*}
    \frac{\partial \av^\top \vv}{\partial \xv} = \av^\top \frac{\partial \vv}{\partial \xv}, ~ \frac{\partial \av^\top \xv}{\partial \xv} = \av^\top \frac{\partial \xv}{\partial \xv} = \av^\top, ~ \frac{\partial \bv^\top \Av \xv}{\partial \xv} = \bv^\top \Av
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 标量对向量求导

$$
\begin{align*}
    \frac{\partial \uv^\top \Av \vv}{\partial \xv} & = \uv^\top \Av \frac{\partial \vv}{\partial \xv} + \vv^\top \Av^\top \frac{\partial \uv}{\partial \xv} \\
    & \overset{\uv = \vv = \xv}{~~ \Longrightarrow ~~} \frac{\partial \xv^\top \Av \xv}{\partial \xv} = \xv^\top \Av \frac{\partial \xv}{\partial \xv} + \xv^\top \Av^\top \frac{\partial \xv}{\partial \xv} = \xv^\top (\Av + \Av^\top) \\
    & \overset{\Av = \bv \av^\top}{~~ \Longrightarrow ~~} \frac{\partial \xv^\top \bv \av^\top \xv}{\partial \xv} = \frac{\partial \av^\top \xv \xv^\top \bv}{\partial \xv} = \xv^\top (\av \bv^\top + \bv \av^\top) \\
    & \overset{\Av = \Iv}{~~ \Longrightarrow ~~} \frac{\partial \xv^\top \xv}{\partial \xv} = \frac{\partial \|\xv\|_2^2}{\partial \xv} = 2 \xv^\top \\
\end{align*}
$$

更一般的有

$$
\begin{align*}
    \frac{\partial (\Av \xv + \bv)^\top \Cv (\Dv \xv + \ev)}{\partial \xv} & = \frac{\partial (\xv^\top \Av^\top \Cv \Dv \xv + \bv^\top \Cv \Dv \xv + \xv^\top \Av^\top \Cv \ev + \bv^\top \ev)}{\partial \xv} \\
    & = \xv^\top (\Av^\top \Cv \Dv + \Dv^\top \Cv^\top \Av) + \bv^\top \Cv \Dv + \ev^\top \Cv^\top \Av                                  \\
    & = (\Dv \xv + \ev)^\top \Cv^\top \Av + (\Av \xv + \bv)^\top \Cv \Dv
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 标量对向量求导

范数也是标量，若$\av$与$\xv$无关，则

$$
\begin{align*}
    \left[ \frac{\partial \| \xv - \av \|_2}{\partial \xv} \right]_i & = \frac{\partial \| \xv - \av \|_2}{\partial x_i} = \frac{\partial \sqrt{\sum_j (x_j - a_j)^2}}{\partial x_i} \\
    & = \frac{1}{2} \frac{2 (x_i - a_i)}{\sqrt{\sum_j (x_j - a_j)^2}} = \frac{x_i - a_i}{\| \xv - \av \|_2} \\
    & \Longrightarrow \class{blue}{\frac{\partial \| \xv - \av \|_2}{\partial \xv} = \frac{(\xv - \av)^\top}{\| \xv - \av \|_2}}
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide data-notes="" -->

GNN-HEADER 大纲

<div class="sparse">

向量对标量求导

标量对向量求导

<span class="blue">向量对向量求导</span>

矩阵对标量求导

标量对矩阵求导

</div>

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="注意第一项是标量乘以雅可比矩阵，第二项是列向量乘以行向量" -->

GNN-HEADER 向量对向量求导

若$\Av$与$\xv$无关，前面已得向量对标量的求导结果$\frac{\partial \Av \uv}{\partial x} = \Av \frac{\partial \uv}{\partial x}$，于是

$$
\begin{align*}
    \left[ \frac{\partial \Av \uv}{\partial \xv} \right]_{:,j} = \frac{\partial \Av \uv}{\partial x_j} = \Av \frac{\partial \uv}{\partial x_j} = \left[ \Av \frac{\partial \uv}{\partial \xv} \right]_{:,j} & \Longrightarrow \class{blue}{\frac{\partial \Av \uv}{\partial \xv} = \Av \frac{\partial \uv}{\partial \xv}} \\
    & \overset{\uv = \xv}{\Longrightarrow} \frac{\partial \Av \xv}{\partial \xv} = \Av \frac{\partial \xv}{\partial \xv} = \Av
\end{align*}
$$

对神经网络第$l$层$\zv_l = \Wv_l ~ \av_{l-1} + \bv_l$，易知有$\frac{\partial \zv_l}{\partial \av_{l-1}} = \frac{\partial (\Wv_l ~ \av_{l-1})}{\partial \av_{l-1}} = \Wv_l$

<div class="bottom2"></div>

若$v = v(\xv)$，则

$$
\begin{align*}
    \left[ \frac{\partial v \uv}{\partial \xv} \right]_{ij} & = \frac{\partial v u_i}{\partial x_j} = v \frac{\partial u_i}{\partial x_j} + u_i \frac{\partial v}{\partial x_j} = v \left[ \frac{\partial \uv}{\partial \xv} \right]_{ij} + \left[ \uv \frac{\partial v}{\partial \xv} \right]_{ij} \\
    & \Longrightarrow \class{blue}{\frac{\partial v \uv}{\partial \xv} = v \frac{\partial \uv}{\partial \xv} + \uv \frac{\partial v}{\partial \xv}}
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 向量对向量求导

若$\av$与$\xv$无关，结合

$$
\begin{align*}
    \class{blue}{\frac{\partial \| \xv - \av \|_2}{\partial \xv^\top} = \frac{\xv - \av}{\| \xv - \av \|_2}}
\end{align*}
$$

可得

$$
\begin{align*}
    & \left[ \frac{\partial}{\partial \xv} \frac{\xv - \av}{\| \xv - \av \|_2} \right]_{ij} = \frac{\partial}{\partial x_j} \frac{x_i - a_i}{\| \xv - \av \|_2} \\
    & \qquad = \frac{\delta_{ij} \|\xv - \av\|_2}{\| \xv - \av \|_2^2} - \frac{x_i - a_i}{\| \xv - \av \|_2^2} \frac{\partial \| \xv - \av \|_2}{\partial x_j} \\
    & \qquad = \frac{\delta_{ij}}{\| \xv - \av \|_2} - \frac{x_i - a_i}{\| \xv - \av \|_2^2} \frac{x_j - a_j}{\| \xv - \av \|_2} \\
    & \qquad \Longrightarrow \class{blue}{\frac{\partial^2 \| \xv - \av \|_2}{\partial \xv \partial \xv^\top} = \frac{\partial}{\partial \xv} \frac{\xv - \av}{\| \xv - \av \|_2} = \frac{\Iv}{\| \xv - \av \|_2} - \frac{(\xv - \av)(\xv - \av)^\top}{\| \xv - \av \|_2^3}}
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide data-notes="" -->

GNN-HEADER 大纲

<div class="sparse">

向量对标量求导

标量对向量求导

向量对向量求导

<span class="blue">矩阵对标量求导</span>

标量对矩阵求导

</div>

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 矩阵对标量求导

若$u = u(x)$，$\Vv = \Vv(x)$，则

$$
\begin{align*}
    \left[ \frac{\partial u \Vv}{\partial x} \right]_{ij} & = \frac{\partial u v_{ij}}{\partial x} = \frac{\partial u}{\partial x} v_{ij} + u \frac{\partial v_{ij}}{\partial x} = \frac{\partial u}{\partial x} \left[ \Vv \right]_{ij} + u \left[ \frac{\partial \Vv}{\partial x} \right]_{ij} \\
    & \Longrightarrow \class{blue}{\frac{\partial u \Vv}{\partial x} = \frac{\partial u}{\partial x} \Vv + u \frac{\partial \Vv}{\partial x}}
\end{align*}
$$

若乘积求导法则中的$\Uv$或$\Vv$可继续分解，则

$$
\begin{align*}
    \frac{\partial (\Uv \Vv)}{\partial x} & = \frac{\partial \Uv}{\partial x} \Vv + \Uv \frac{\partial \Vv}{\partial x} \\
    & \Downarrow \\
    \class{blue}{\frac{\partial (\Uv \Vv \Wv)}{\partial x}} & = \frac{\partial \Uv}{\partial x} \Vv \Wv + \Uv \frac{\partial \Vv \Wv}{\partial x} = \frac{\partial \Uv}{\partial x} \Vv \Wv + \Uv \left( \frac{\partial \Vv}{\partial x} \Wv + \Vv \frac{\partial \Wv}{\partial x} \right) \\
    & = \class{blue}{\frac{\partial \Uv}{\partial x} \Vv \Wv + \Uv \frac{\partial \Vv}{\partial x} \Wv + \Uv \Vv \frac{\partial \Wv}{\partial x}}
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 矩阵对标量求导

$$
\begin{align}
    \class{blue}{\frac{\partial (\Uv \Vv \Wv)}{\partial x} = \frac{\partial \Uv}{\partial x} \Vv \Wv + \Uv \frac{\partial \Vv}{\partial x} \Wv + \Uv \Vv \frac{\partial \Wv}{\partial x}}
\end{align}
$$

由此可知若$\Av$、$\Bv$与$x$无关，则

$$
\begin{align*}
    \frac{\partial \Av \Uv \Bv}{\partial x} = \Av \frac{\partial \Uv}{\partial x} \Bv
\end{align*}
$$

当$\Uv$为方阵、$n$为正整数时有

$$
\begin{align}
    \class{blue}{\frac{\partial \Uv^n}{\partial x}} & = \Uv^{n-1} \frac{\partial \Uv}{\partial x} + \Uv^{n-2} \frac{\partial \Uv}{\partial x} \Uv + \cdots + \Uv \frac{\partial \Uv}{\partial x} \Uv^{n-2} + \frac{\partial \Uv}{\partial x} \Uv^{n-1} \\
    & = \class{blue}{\sum_{i \in [n]} \Uv^{i-1} \frac{\partial \Uv}{\partial x} \Uv^{n-i}}
\end{align}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide data-notes="" -->

GNN-HEADER 矩阵对标量求导

令乘积求导法则中的$\Vv = \Uv^{-1}$可得

$$
\begin{align} \label{eq: inverse}
    \zerov = \frac{\partial \Iv}{\partial x} & = \frac{\partial \Uv \Uv^{-1}}{\partial x} = \Uv \frac{\partial \Uv^{-1}}{\partial x} + \frac{\partial \Uv}{\partial x} \Uv^{-1} \\
    & \Longrightarrow \class{blue}{\frac{\partial \Uv^{-1}}{\partial x} = - \Uv^{-1} \frac{\partial \Uv}{\partial x} \Uv^{-1}}
\end{align}
$$

结合链式法则情形三可知

$$
\begin{align*}
    \class{blue}{\frac{\partial [\Xv^{-1}]_{kl}}{\partial x_{ij}}} & = \tr \left( \frac{\partial [\Xv^{-1}]_{kl}}{\partial \Xv^{-1}} \frac{\partial \Xv^{-1}}{\partial x_{ij}} \right) = - \tr \left( \Ev_{lk} \Xv^{-1} \frac{\partial \Xv}{\partial x_{ij}} \Xv^{-1} \right) \\
    & = - \tr ( \Xv^{-1} \Ev_{lk} \Xv^{-1} \Ev_{ij} ) = - [\Xv^{-1} \Ev_{lk} \Xv^{-1}]_{ji} \\
    & = - \sum_p \sum_q [\Xv^{-1}]_{jp} [\Ev_{lk}]_{pq} [\Xv^{-1}]_{qi} = \class{blue}{- [\Xv^{-1}]_{jl} [\Xv^{-1}]_{ki}}
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 矩阵对标量求导

$$
\begin{align*}
    \class{blue}{\frac{\partial \Uv^{-1}}{\partial x} = - \Uv^{-1} \frac{\partial \Uv}{\partial x} \Uv^{-1}}
\end{align*}
$$

结合$\class{blue}{\frac{\partial (\Uv \Vv \Wv)}{\partial x} = \frac{\partial \Uv}{\partial x} \Vv \Wv + \Uv \frac{\partial \Vv}{\partial x} \Wv + \Uv \Vv \frac{\partial \Wv}{\partial x}}$可得海森矩阵

$$
\begin{align*}
    & \class{blue}{\frac{\partial^2 \Uv^{-1}}{\partial x \partial y}} = \frac{\partial}{\partial y} \left( - \Uv^{-1} \frac{\partial \Uv}{\partial x} \Uv^{-1} \right) \\
    & \qquad = - \frac{\partial \Uv^{-1}}{\partial y} \frac{\partial \Uv}{\partial x} \Uv^{-1} - \Uv^{-1} \frac{\partial^2 \Uv}{\partial x \partial y} \Uv^{-1} - \Uv^{-1} \frac{\partial \Uv}{\partial x} \frac{\partial \Uv^{-1}}{\partial y} \\
    & \qquad = \Uv^{-1} \frac{\partial \Uv}{\partial y} \Uv^{-1} \frac{\partial \Uv}{\partial x} \Uv^{-1} - \Uv^{-1} \frac{\partial^2 \Uv}{\partial x \partial y} \Uv^{-1} + \Uv^{-1} \frac{\partial \Uv}{\partial x} \Uv^{-1} \frac{\partial \Uv}{\partial y} \Uv^{-1}                                                                          \\
    & \qquad = \class{blue}{\Uv^{-1} \left( \frac{\partial \Uv}{\partial y} \Uv^{-1} \frac{\partial \Uv}{\partial x} - \frac{\partial^2 \Uv}{\partial x \partial y} + \frac{\partial \Uv}{\partial x} \Uv^{-1} \frac{\partial \Uv}{\partial y} \right) \Uv^{-1}}
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide data-notes="" -->

GNN-HEADER 矩阵对标量求导

矩阵除了常规的乘积外，还有哈达玛积和克罗内克积

<br>

设$\Uv, \Vv \in \Rbb^{m \times n}$，则

$$
\begin{align*}
    & \class{blue}{\frac{\partial (\Uv \circ \Vv)}{\partial x}} = \begin{bmatrix}
        \frac{\partial u_{11} v_{11}}{\partial x} & \cdots & \frac{\partial u_{1n} v_{1n}}{\partial x} \\
        \vdots                                    & \ddots & \vdots                                    \\
        \frac{\partial u_{m1} v_{m1}}{\partial x} & \cdots & \frac{\partial u_{mn} v_{mn}}{\partial x} \\
    \end{bmatrix}                                                                   \\
    & \qquad = \begin{bmatrix}
        \frac{\partial u_{11}}{\partial x} v_{11} & \cdots & \frac{\partial u_{1n}}{\partial x} v_{1n} \\
        \vdots                                    & \ddots & \vdots                                    \\
        \frac{\partial u_{m1}}{\partial x} v_{m1} & \cdots & \frac{\partial u_{mn}}{\partial x} v_{mn} \\
    \end{bmatrix} + \begin{bmatrix}
        u_{11} \frac{\partial v_{11}}{\partial x} & \cdots & u_{1n} \frac{\partial v_{1n}}{\partial x} \\
        \vdots                                    & \ddots & \vdots                                    \\
        u_{m1} \frac{\partial v_{m1}}{\partial x} & \cdots & u_{mn} \frac{\partial v_{mn}}{\partial x} \\
    \end{bmatrix}                                      \\
    & \qquad = \class{blue}{\frac{\partial \Uv}{\partial x} \circ \Vv + \Uv \circ \frac{\partial \Vv}{\partial x}}
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 矩阵对标量求导

$$
\begin{align*}
    & \class{blue}{\frac{\partial (\Uv \otimes \Vv)}{\partial x}} = \begin{bmatrix}
        \frac{\partial u_{11} \Vv}{\partial x} & \cdots & \frac{\partial u_{1n} \Vv}{\partial x} \\
        \vdots                                 & \ddots & \vdots                                 \\
        \frac{\partial u_{m1} \Vv}{\partial x} & \cdots & \frac{\partial u_{mn} \Vv}{\partial x} \\
    \end{bmatrix}                                                                       \\
    & \qquad = \begin{bmatrix}
        \frac{\partial u_{11}}{\partial x} \Vv + u_{11} \frac{\partial \Vv}{\partial x} & \cdots & \frac{\partial u_{1n}}{\partial x} \Vv + u_{1n} \frac{\partial \Vv}{\partial x} \\
        \vdots                                                                          & \ddots & \vdots                                                                          \\
        \frac{\partial u_{m1}}{\partial x} \Vv + u_{m1} \frac{\partial \Vv}{\partial x} & \cdots & \frac{\partial u_{mn}}{\partial x} \Vv + u_{mn} \frac{\partial \Vv}{\partial x} \\
    \end{bmatrix}                                                                       \\
    & \qquad = \begin{bmatrix}
        \frac{\partial u_{11}}{\partial x} \Vv & \cdots & \frac{\partial u_{1n}}{\partial x} \Vv \\
        \vdots                                 & \ddots & \vdots                                 \\
        \frac{\partial u_{m1}}{\partial x} \Vv & \cdots & \frac{\partial u_{mn}}{\partial x} \Vv \\
    \end{bmatrix} + \begin{bmatrix}
        u_{11} \frac{\partial \Vv}{\partial x} & \cdots & u_{1n} \frac{\partial \Vv}{\partial x} \\
        \vdots                                 & \ddots & \vdots                                 \\
        u_{m1} \frac{\partial \Vv}{\partial x} & \cdots & u_{mn} \frac{\partial \Vv}{\partial x} \\
    \end{bmatrix}                                          \\
    & \qquad = \class{blue}{\frac{\partial \Uv}{\partial x} \otimes \Vv + \Uv \otimes \frac{\partial \Vv}{\partial x}}
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 矩阵对标量求导

设$g(x) = a_0 + a_1 x + a_2 x^2 + \cdots$，若$\Av$为与$x$无关的方阵，记

$$
\begin{align*}
    g (x \Av)  & = a_0 \Iv + a_1 x \Av + a_2 x^2 \Av^2 + a_3 x^3 \Av^3 + \cdots \\
    g' (x \Av) & = a_1 \Iv + 2 a_2 x \Av + 3 a_3 x^2 \Av^2 + \cdots
\end{align*}
$$

易知有

$$
\begin{align*}
    \class{blue}{\frac{\partial g(x \Av)}{\partial x}} & = a_1 \Av + 2 a_2 x \Av^2 + 3 a_3 x^2 \Av^3 + \cdots                             \\
    & = \Av (a_1 \Iv + 2 a_2 x \Av + 3 a_3 x^2 \Av^2 + \cdots) = \class{blue}{\Av g' (x \Av)} \\
    & = (a_1 \Iv + 2 a_2 x \Av + 3 a_3 x^2 \Av^2 + \cdots) \Av = \class{blue}{g' (x \Av) \Av}
\end{align*}
$$

对于$e^x$、$\ln x$、$\sin x$、$\cos x$，上式依然适用，例如

$$
\begin{align*}
    \frac{\partial e^{x \Av}}{\partial x} = \Av e^{x \Av} = e^{x \Av} \Av
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide data-notes="" -->

GNN-HEADER 大纲

<div class="sparse">

向量对标量求导

标量对向量求导

向量对向量求导

矩阵对标量求导

<span class="blue">标量对矩阵求导</span>

</div>

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 迹对矩阵求导

矩阵常见的标量函数有<span class="blue">迹</span>和<span class="blue">行列式</span>，二次型可以归为迹来处理

若$a$与$\Xv$无关，$\Uv = \Uv(\Xv)$，$\Vv = \Vv(\Xv)$，则以下结论是显然的：

$$
\begin{align*}
    \frac{\partial \tr(\Xv)}{\partial \Xv} = \Iv, ~ \frac{\partial \tr(\Uv+\Vv)}{\partial \Xv} = \frac{\partial \tr(\Uv)}{\partial \Xv} + \frac{\partial \tr(\Vv)}{\partial \Xv}, ~ \frac{\partial \tr(a \Uv)}{\partial \Xv} = a \frac{\partial \tr(\Uv)}{\partial \Xv}
\end{align*}
$$

对于乘积有

$$
\begin{align*}
    \left[ \frac{\partial \tr(\Uv \Vv)}{\partial \Xv} \right]_{ij} & = \class{blue}{\frac{\partial \tr(\Uv \Vv)}{\partial x_{ji}}} = \sum_p \sum_q \left( \frac{\partial u_{pq}}{\partial x_{ji}} v_{qp} + u_{pq} \frac{\partial v_{qp}}{\partial x_{ji}} \right) \\
    & = \class{blue}{\tr \left( \frac{\partial \Uv}{\partial x_{ji}} \Vv \right) + \tr \left( \Uv \frac{\partial \Vv}{\partial x_{ji}} \right)} = \tr \left( \frac{\partial \Uv \Vv}{\partial x_{ji}} \right)
\end{align*}
$$

由此可知<span class="blue">迹和求导的顺序可以交换</span>

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 迹对矩阵求导

$$
\begin{align*}
    \left[ \frac{\partial \tr(\Uv \Vv)}{\partial \Xv} \right]_{ij} = \frac{\partial \tr(\Uv \Vv)}{\partial x_{ji}} = \tr \left( \frac{\partial \Uv \Vv}{\partial x_{ji}} \right)
\end{align*}
$$

取$\Uv = \Bv \Av$与$\Xv$无关，$\Vv = \Xv$，则

$$
\begin{align*}
    \left[ \frac{\partial \tr(\Bv \Av \Xv)}{\partial \Xv} \right]_{ij} & = \tr \left( \Bv \Av \frac{\partial \Xv}{\partial x_{ji}} \right) = \tr ( \Bv \Av \Ev_{ji} ) = [\Bv \Av]_{ij} \\
    & \Longrightarrow \frac{\partial \tr(\Bv \Av \Xv)}{\partial \Xv} = \frac{\partial \tr(\Av \Xv \Bv)}{\partial \Xv} = \frac{\partial \tr(\Xv \Bv \Av)}{\partial \Xv} = \Bv \Av
\end{align*}
$$

取$\Uv = \Bv \Av$与$\Xv$无关，$\Vv = \Xv^\top$，则

$$
\begin{align*}
    \frac{\partial \tr(\Av \Xv^\top \Bv)}{\partial \Xv} = \frac{\partial \tr(\Xv^\top \Bv \Av)}{\partial \Xv} = \frac{\partial \tr(\Bv \Av \Xv^\top)}{\partial \Xv} = \frac{\partial \tr(\Xv \Av^\top \Bv^\top)}{\partial \Xv} = \Av^\top \Bv^\top
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide data-notes="" -->

GNN-HEADER 迹对矩阵求导

$$
\begin{align*}
    \left[ \frac{\partial \tr(\Uv \Vv)}{\partial \Xv} \right]_{ij} = \frac{\partial \tr(\Uv \Vv)}{\partial x_{ji}} = \tr \left( \frac{\partial \Uv \Vv}{\partial x_{ji}} \right)
\end{align*}
$$

取$\Uv = \Av$与$\Xv$无关，$\Vv = \Xv \Xv^\top$，则

$$
\begin{align*}
    \left[ \frac{\partial \tr(\Av \Xv \Xv^\top)}{\partial \Xv} \right]_{ij} & = \tr \left( \Av \frac{\partial \Xv \Xv^\top}{\partial x_{ji}} \right) = \tr \left( \Av \frac{\partial \Xv}{\partial x_{ji}} \Xv^\top \right) + \tr \left( \Av \Xv \frac{\partial \Xv^\top}{\partial x_{ji}} \right) \\
    & = \tr(\Av \Ev_{ji} \Xv^\top) + \tr(\Av \Xv \Ev_{ij}) \\
    & = [\Xv^\top \Av]_{ij} + [\Av \Xv]_{ji}
\end{align*}
$$

从而

$$
\begin{align*}
    \frac{\partial \tr(\Av \Xv \Xv^\top)}{\partial \Xv} & = \frac{\partial \tr(\Xv^\top \Av \Xv)}{\partial \Xv} = \frac{\partial \tr(\Xv \Xv^\top \Av)}{\partial \Xv} \\
    & = \Xv^\top \Av + \Xv^\top \Av^\top = \Xv^\top (\Av + \Av^\top)
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 迹对矩阵求导

$$
\begin{align*}
    \left[ \frac{\partial \tr(\Uv \Vv)}{\partial \Xv} \right]_{ij} = \frac{\partial \tr(\Uv \Vv)}{\partial x_{ji}} = \tr \left( \frac{\partial \Uv \Vv}{\partial x_{ji}} \right)
\end{align*}
$$

取$\Uv = \Av$与$\Xv$无关，$\Vv = \Xv^\top \Xv$，则

$$
\begin{align*}
    \left[ \frac{\partial \tr(\Av \Xv^\top \Xv)}{\partial \Xv} \right]_{ij} & = \tr \left( \Av \frac{\partial \Xv^\top \Xv}{\partial x_{ji}} \right) = \tr \left( \Av \frac{\partial \Xv^\top}{\partial x_{ji}} \Xv \right) + \tr \left( \Av \Xv^\top \frac{\partial \Xv}{\partial x_{ji}} \right) \\
    & = \tr(\Av \Ev_{ij} \Xv) + \tr(\Av \Xv^\top \Ev_{ji}) \\
    & = [\Xv \Av]_{ji} + [\Av \Xv^\top]_{ij}
\end{align*}
$$

从而

$$
\begin{align*}
    \frac{\partial \tr(\Av \Xv^\top \Xv)}{\partial \Xv} = \frac{\partial \tr(\Xv \Av \Xv^\top)}{\partial \Xv} = \frac{\partial \tr(\Xv^\top \Xv \Av)}{\partial \Xv} = (\Av + \Av^\top) \Xv^\top
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="本页最后一个式子解决了极大似然里的问题" -->

GNN-HEADER 迹对矩阵求导

$$
\begin{align*}
    \left[ \frac{\partial \tr(\Uv \Vv)}{\partial \Xv} \right]_{ij} = \frac{\partial \tr(\Uv \Vv)}{\partial x_{ji}} = \tr \left( \frac{\partial \Uv \Vv}{\partial x_{ji}} \right)
\end{align*}
$$

取$\Uv = \Bv \Av$与$\Xv$无关，$\Vv = \Xv^{-1}$，结合

$$
\begin{align*}
    \frac{\partial \Uv^{-1}}{\partial x} = - \Uv^{-1} \frac{\partial \Uv}{\partial x} \Uv^{-1}
\end{align*}
$$

可得

$$
\begin{align*}
    & \left[ \frac{\partial \tr(\Bv \Av \Xv^{-1})}{\partial \Xv} \right]_{ij} = \tr \left( \Bv \Av \frac{\partial \Xv^{-1}}{\partial x_{ji}} \right) = \tr \left( - \Bv \Av \Xv^{-1} \frac{\partial \Xv}{\partial x_{ji}} \Xv^{-1} \right) \\
    & \quad = - \tr \left( \Xv^{-1} \Bv \Av \Xv^{-1} \Ev_{ji} \right) = - [\Xv^{-1} \Bv \Av \Xv^{-1}]_{ij} \\
    & \quad \Longrightarrow \frac{\partial \tr(\Bv \Av \Xv^{-1})}{\partial \Xv} = \frac{\partial \tr(\Av \Xv^{-1} \Bv)}{\partial \Xv} = \frac{\partial \tr(\Xv^{-1} \Bv \Av)}{\partial \Xv} = - \Xv^{-1} \Bv \Av \Xv^{-1}
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide data-notes="" -->

GNN-HEADER 迹对矩阵求导

$$
\begin{align*}
    \left[ \frac{\partial \tr(\Uv \Vv)}{\partial \Xv} \right]_{ij} = \frac{\partial \tr(\Uv \Vv)}{\partial x_{ji}} = \tr \left( \frac{\partial \Uv \Vv}{\partial x_{ji}} \right)
\end{align*}
$$

取$\Uv = \Iv$，$\Vv = (\Xv + \Av)^{-1}$，结合$\frac{\partial \Uv^{-1}}{\partial x} = - \Uv^{-1} \frac{\partial \Uv}{\partial x} \Uv^{-1}$可得

$$
\begin{align*}
    \left[ \frac{\partial \tr(\Xv + \Av)^{-1}}{\partial \Xv} \right]_{ij} & = \tr \left( \frac{\partial (\Xv + \Av)^{-1}}{\partial x_{ji}} \right) \\
    & = - \tr \left( (\Xv + \Av)^{-1} \frac{\partial (\Xv + \Av)}{\partial x_{ji}} (\Xv + \Av)^{-1} \right) \\
    & = - \tr \left( (\Xv + \Av)^{-1} (\Xv + \Av)^{-1} \Ev_{ji}  \right) \\
    & = - [(\Xv + \Av)^{-1} (\Xv + \Av)^{-1}]_{ij} \\
    & \Longrightarrow \frac{\partial \tr(\Xv + \Av)^{-1}}{\partial \Xv} = - (\Xv + \Av)^{-1} (\Xv + \Av)^{-1}
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 迹对矩阵求导

$$
\begin{align*}
    \left[ \frac{\partial \tr(\Uv \Vv)}{\partial \Xv} \right]_{ij} = \frac{\partial \tr(\Uv \Vv)}{\partial x_{ji}} = \tr \left( \frac{\partial \Uv \Vv}{\partial x_{ji}} \right)
\end{align*}
$$

取$\Uv = \Av \Xv \Bv$，$\Vv = \Xv^\top \Cv$，其中$\Av$、$\Bv$、$\Cv$与$\Xv$无关，则

$$
\begin{align*}
    & \left[ \frac{\partial \tr(\Av \Xv \Bv \Xv^\top \Cv)}{\partial \Xv} \right]_{ij} = \tr \left( \frac{\partial \Av \Xv \Bv}{\partial x_{ji}} \Xv^\top \Cv \right) + \tr \left( \Av \Xv \Bv \frac{\partial \Xv^\top \Cv}{\partial x_{ji}} \right) \\
    & \qquad = \tr \left( \Av \Ev_{ji} \Bv \Xv^\top \Cv \right) + \tr \left( \Av \Xv \Bv \Ev_{ij} \Cv \right) = [\Bv \Xv^\top \Cv \Av]_{ij} + [\Cv \Av \Xv \Bv]_{ji} \\
    & \qquad \Longrightarrow \frac{\partial \tr(\Av \Xv \Bv \Xv^\top \Cv)}{\partial \Xv} = \Bv \Xv^\top \Cv \Av + \Bv^\top \Xv^\top \Av^\top \Cv^\top
\end{align*}
$$

令$\Xv \leftarrow \Xv^\top$，于是只需对结果取转置即有

$$
\begin{align*}
    \frac{\partial \tr(\Av \Xv^\top \Bv \Xv \Cv)}{\partial \Xv} = \Cv \Av \Xv^\top \Bv + \Av^\top \Cv^\top \Xv^\top \Bv^\top
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 迹对矩阵求导

$$
\begin{align*}
    \left[ \frac{\partial \tr(\Uv \Vv)}{\partial \Xv} \right]_{ij} = \frac{\partial \tr(\Uv \Vv)}{\partial x_{ji}} = \tr \left( \frac{\partial \Uv \Vv}{\partial x_{ji}} \right)
\end{align*}
$$

取$\Uv = \Av \Xv \Bv$，$\Vv = \Xv^\top \Cv$，其中$\Av$、$\Bv$、$\Cv$与$\Xv$无关，则

$$
\begin{align*}
    & \left[ \frac{\partial \tr(\Av \Xv \Bv \Xv^\top \Cv)}{\partial \Xv} \right]_{ij} = \tr \left( \frac{\partial \Av \Xv \Bv}{\partial x_{ji}} \Xv^\top \Cv \right) + \tr \left( \Av \Xv \Bv \frac{\partial \Xv^\top \Cv}{\partial x_{ji}} \right) \\
    & \qquad = \tr \left( \Av \Ev_{ji} \Bv \Xv^\top \Cv \right) + \tr \left( \Av \Xv \Bv \Ev_{ij} \Cv \right) = [\Bv \Xv^\top \Cv \Av]_{ij} + [\Cv \Av \Xv \Bv]_{ji} \\
    & \qquad \Longrightarrow \frac{\partial \tr(\Av \Xv \Bv \Xv^\top \Cv)}{\partial \Xv} = \Bv \Xv^\top \Cv \Av + \Bv^\top \Xv^\top \Av^\top \Cv^\top
\end{align*}
$$

令$\Xv \leftarrow \Xv^\top$，于是只需对结果取转置即有

$$
\begin{align*}
    \frac{\partial \tr(\Av \Xv^\top \Bv \Xv \Cv)}{\partial \Xv} = \Cv \Av \Xv^\top \Bv + \Av^\top \Cv^\top \Xv^\top \Bv^\top
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide data-notes="" -->

GNN-HEADER 迹对矩阵求导

$$
\begin{align*}
    \left[ \frac{\partial \tr(\Uv \Vv)}{\partial \Xv} \right]_{ij} = \frac{\partial \tr(\Uv \Vv)}{\partial x_{ji}} = \tr \left( \frac{\partial \Uv \Vv}{\partial x_{ji}} \right)
\end{align*}
$$

取$\Uv = \Bv \Av$与$\Xv$无关，$\Vv = \Xv^n$，其中$n$是正整数，于是

$$
\begin{align*}
    & \left[ \frac{\partial \tr(\Bv \Av \Xv^n)}{\partial \Xv} \right]_{ij} = \tr \left( \Bv \Av \frac{\partial \Xv^n}{\partial x_{ji}} \right) = \tr \left( \Bv \Av \sum_{k \in [n]} \Xv^{k-1} \frac{\partial \Xv}{\partial x_{ji}} \Xv^{n-k} \right) \\
    & ~ = \sum_{k \in [n]} \tr \left( \Bv \Av \Xv^{k-1} \frac{\partial \Xv}{\partial x_{ji}} \Xv^{n-k} \right) \\
    & ~ = \sum_{k \in [n]} \tr ( \Xv^{n-k} \Bv \Av \Xv^{k-1} \Ev_{ji} ) = \sum_{k \in [n]} [\Xv^{n-k} \Bv \Av \Xv^{k-1}]_{ij} \\
    & ~ \Longrightarrow \frac{\partial \tr(\Bv \Av \Xv^n)}{\partial \Xv} = \frac{\partial \tr(\Av \Xv^n \Bv)}{\partial \Xv} = \frac{\partial \tr(\Xv^n \Bv \Av)}{\partial \Xv} = \sum_{k \in [n]} \Xv^{n-k} \Bv \Av \Xv^{k-1}
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 迹对矩阵求导

$$
\begin{align*}
    \frac{\partial \tr(\Bv \Av \Xv^n)}{\partial \Xv} = \frac{\partial \tr(\Av \Xv^n \Bv)}{\partial \Xv} = \frac{\partial \tr(\Xv^n \Bv \Av)}{\partial \Xv} = \sum_{k \in [n]} \Xv^{n-k} \Bv \Av \Xv^{k-1}
\end{align*}
$$

进一步若$\Av = \Bv = \Iv$，则

$$
\begin{align*}
    \frac{\partial \tr(\Xv^n)}{\partial \Xv} = \sum_{k \in [n]} \Xv^{n-k} \Xv^{k-1} = \sum_{k \in [n]} \Xv^{n-1} = n \Xv^{n-1}
\end{align*}
$$

不难发现形式上和单变量求导公式是一样的，类似的记

$$
\begin{align*}
    e^{\Xv}  & = \Iv + \Xv + \frac{\Xv^2}{2!} + \frac{\Xv^3}{3!} + \cdots              \\
    \sin \Xv & = \Xv - \frac{\Xv^3}{3!} + \frac{\Xv^5}{5!} - \cdots, \quad \cos \Xv = \Iv - \frac{\Xv^2}{2!} + \frac{\Xv^4}{4!} - \frac{\Xv^6}{6!} + \cdots
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 迹对矩阵求导

$$
\begin{align*}
    \frac{\partial \tr(e^{\Xv})}{\partial \Xv} & = \frac{\partial }{\partial \Xv} \tr \left( \Iv + \Xv + \frac{\Xv^2}{2!} + \frac{\Xv^3}{3!} + \cdots \right) \\
    & = \frac{\partial \tr (\Iv)}{\partial \Xv} + \frac{\partial \tr (\Xv)}{\partial \Xv} + \frac{1}{2!} \frac{\partial \tr (\Xv^2)}{\partial \Xv} + \frac{1}{3!} \frac{\partial \tr (\Xv^3)}{\partial \Xv} + \cdots \\
    & = \Iv + \Xv + \frac{\Xv^2}{2!} + \cdots = e^{\Xv} \\
    \frac{\partial \tr(\sin \Xv)}{\partial \Xv} & = \frac{\partial }{\partial \Xv} \tr \left( \Xv - \frac{\Xv^3}{3!} + \frac{\Xv^5}{5!} - \cdots \right) \\
    & = \Iv - \frac{\Xv^2}{2!} + \frac{\Xv^4}{4!} - \cdots = \cos \Xv \\
    \frac{\partial \tr(\cos \Xv)}{\partial \Xv} & = \frac{\partial }{\partial \Xv} \tr \left( \Iv - \frac{\Xv^2}{2!} + \frac{\Xv^4}{4!} - \frac{\Xv^6}{6!} + \cdots \right) \\
    & = - \Xv + \frac{\Xv^3}{3!} - \frac{\Xv^5}{5!} + \cdots = - \sin \Xv
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 迹对矩阵求导

$$
\begin{align*}
    \left[ \frac{\partial \tr(\Uv \Vv)}{\partial \Xv} \right]_{ij} = \frac{\partial \tr(\Uv \Vv)}{\partial x_{ji}} = \tr \left( \frac{\partial \Uv \Vv}{\partial x_{ji}} \right)
\end{align*}
$$

取$\Uv = \Iv$，$\Vv = \Av \otimes \Xv$，则

$$
\begin{align*}
    & \left[ \frac{\partial \tr(\Av \otimes \Xv)}{\partial \Xv} \right]_{ij} = \tr \left( \frac{\partial \Av \otimes \Xv}{\partial x_{ji}} \right) = \tr \left( \Av \otimes \frac{\partial \Xv}{\partial x_{ji}} \right) \\
    & ~ = \tr ( \Av \otimes \Ev_{ji} ) = \tr(\Av) \delta_{ij} \Longrightarrow \frac{\partial \tr(\Av \otimes \Xv)}{\partial \Xv} = \tr(\Av) \Iv
\end{align*}
$$

取$\Uv = \Iv$，$\Vv = \Xv \otimes \Xv$，则

$$
\begin{align*}
    & \left[ \frac{\partial \tr(\Xv \otimes \Xv)}{\partial \Xv} \right]_{ij} = \tr \left( \frac{\partial \Xv \otimes \Xv}{\partial x_{ji}} \right) = \tr \left( \frac{\partial \Xv}{\partial x_{ji}} \otimes \Xv + \Xv \otimes \frac{\partial \Xv}{\partial x_{ji}} \right) \\
    & ~ = \tr ( \Ev_{ji} \otimes \Xv ) + \tr ( \Xv \otimes \Ev_{ji} ) = 2 \tr(\Xv) \delta_{ij} \Longrightarrow \frac{\partial \tr(\Xv \otimes \Xv)}{\partial \Xv} = 2 \tr(\Xv) \Iv
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide data-notes="" -->

GNN-HEADER 行列式对矩阵求导

设$\Xv \in \Rbb^{m \times n}, \Av \in \Rbb^{l \times m}, \Bv \in \Rbb^{n \times l}, \Yv = \Av \Xv \Bv \in \Rbb^{l \times l}$，$\Av$、$\Bv$与$\Xv$无关

$$
\begin{align*}
    \left[ \frac{\partial |\Av \Xv \Bv|}{\partial \Xv} \right]_{ij} = \frac{\partial |\Yv|}{\partial x_{ji}} = \sum_p \sum_q \frac{\partial |\Yv|}{\partial y_{pq}}\frac{\partial y_{pq}}{\partial x_{ji}} = \tr \left( \frac{\partial |\Yv|}{\partial \Yv} \frac{\partial \Yv}{\partial x_{ji}} \right)
\end{align*}
$$

记$y_{ji}$有微小增量$\epsilon$后的矩阵为$\Yv(y_{ji} + \epsilon)$，根据第$j$行拉普拉斯展开

$$
\begin{align*}
    |\Yv(y_{ji} + \epsilon)| - |\Yv| = \epsilon ~ C_{ji}
\end{align*}
$$

其中$C_{ji}$是关于$y_{ji}$的<span class="blue">代数余子式</span>，于是

$$
\begin{align*}
    \left[ \frac{\partial |\Yv|}{\partial \Yv} \right]_{ij} & = \frac{\partial |\Yv|}{\partial y_{ji}} = \lim_{\epsilon \rightarrow 0} \frac{|\Yv(y_{ji} + \epsilon)| - |\Yv|}{\epsilon} = C_{ji} ~ \Longrightarrow ~ \frac{\partial |\Yv|}{\partial \Yv} = \Yv^*
\end{align*}
$$

其中$\Yv^*$是$\Yv$的<span class="blue">伴随矩阵</span> (adjugate matrix)

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 行列式对矩阵求导

设$\Xv \in \Rbb^{m \times n}, \Av \in \Rbb^{l \times m}, \Bv \in \Rbb^{n \times l}, \Yv = \Av \Xv \Bv \in \Rbb^{l \times l}$，$\Av$、$\Bv$与$\Xv$无关

$$
\begin{align*}
    \left[ \frac{\partial |\Av \Xv \Bv|}{\partial \Xv} \right]_{ij} = \frac{\partial |\Yv|}{\partial x_{ji}} = \sum_p \sum_q \frac{\partial |\Yv|}{\partial y_{pq}}\frac{\partial y_{pq}}{\partial x_{ji}} = \tr \left( \Yv^* \frac{\partial \Yv}{\partial x_{ji}} \right)
\end{align*}
$$

又第二项

$$
\begin{align*}
    \frac{\partial \Yv}{\partial x_{ji}} = \frac{\partial \Av \Xv \Bv}{\partial x_{ji}} = \Av \frac{\partial \Xv}{\partial x_{ji}} \Bv = \Av \Ev_{ji} \Bv
\end{align*}
$$

代入可得

$$
\begin{align*}
    \left[ \frac{\partial |\Av \Xv \Bv|}{\partial \Xv} \right]_{ij} & = \tr (\Yv^* \Av \Ev_{ji} \Bv) = [\Bv \Yv^* \Av]_{ij} \\
    & \Longrightarrow \class{blue}{\frac{\partial |\Av \Xv \Bv|}{\partial \Xv} = \Bv (\Av \Xv \Bv)^* \Av}
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 行列式对矩阵求导

设$\Xv \in \Rbb^{m \times n}, \Av \in \Rbb^{l \times m}, \Bv \in \Rbb^{n \times l}, \Yv = \Av \Xv \Bv \in \Rbb^{l \times l}$，$\Av$、$\Bv$与$\Xv$无关

$$
\begin{align*}
    \class{blue}{\frac{\partial |\Av \Xv \Bv|}{\partial \Xv} = \Bv (\Av \Xv \Bv)^* \Av}
\end{align*}
$$

若$\Xv, \Av, \Bv$均为可逆方阵，则$\Yv = \Av \Xv \Bv$亦为可逆方阵，于是

$$
\begin{align} \label{eq: determinant}
    \frac{\partial |\Av \Xv \Bv|}{\partial \Xv} = \Bv (\Av \Xv \Bv)^* \Av = \Bv |\Av \Xv \Bv| (\Av \Xv \Bv)^{-1} \Av = |\Av \Xv \Bv| \Xv^{-1}
\end{align}
$$

进一步若$\Av = \Bv = \Iv$，则$\frac{\partial |\Xv|}{\partial \Xv} = \Xv^* = |\Xv| \Xv^{-1}$，由此可得

$$
\begin{align*}
    \frac{\partial |\Xv^n|}{\partial \Xv} = \frac{\partial |\Xv|^n}{\partial \Xv} = n |\Xv|^{n-1} \Xv^* = n |\Xv|^n \Xv^{-1} = n |\Xv^n| \Xv^{-1}
\end{align*}
$$

若$a$与$\Xv$无关，则$\frac{\partial \ln |a \Xv|}{\partial \Xv} = \frac{\partial \ln a^m |\Xv|}{\partial \Xv} = \frac{\partial \ln |\Xv|}{\partial \Xv} = \frac{1}{|\Xv|} \frac{\partial |\Xv|}{\partial \Xv} = \frac{\Xv^*}{|\Xv|} = \Xv^{-1}$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 行列式对矩阵求导

设$\Xv \in \Rbb^{m \times n}, \Av \in \Rbb^{m \times m}, \Yv = \Xv^\top \Av \Xv \in \Rbb^{n \times n}$可逆，$\Av$与$\Xv$无关，易知

$$
\begin{align*}
    & \left[ \frac{\partial |\Xv^\top \Av \Xv|}{\partial \Xv} \right]_{ij} = \tr \left( \frac{\partial |\Xv^\top \Av \Xv|}{\partial \Yv} \frac{\partial \Yv}{\partial x_{ji}} \right) = \tr \left( \Yv^* \frac{\partial \Xv^\top \Av \Xv}{\partial x_{ji}} \right) \\
    & = \tr \left( \Yv^* \frac{\partial \Xv^\top}{\partial x_{ji}} \Av \Xv \right) + \tr \left( \Yv^* \Xv^\top \Av \frac{\partial \Xv}{\partial x_{ji}} \right) \\
    & = \tr ( \Yv^* \Ev_{ij} \Av \Xv ) + \tr ( \Yv^* \Xv^\top \Av \Ev_{ji} ) = [\Av \Xv \Yv^*]_{ji} + [\Yv^* \Xv^\top \Av]_{ij}
\end{align*}
$$

于是

$$
\begin{align*}
    \frac{\partial |\Xv^\top \Av \Xv|}{\partial \Xv} & = (\Av \Xv \Yv^*)^\top + \Yv^* \Xv^\top \Av \\
    & = (\Av \Xv |\Xv^\top \Av \Xv| (\Xv^\top \Av \Xv)^{-1})^\top + |\Xv^\top \Av \Xv| (\Xv^\top \Av \Xv)^{-1} \Xv^\top \Av \\
    & = |\Xv^\top \Av \Xv| (\Xv^\top \Av^\top \Xv)^{-1} \Xv^\top \Av^\top + |\Xv^\top \Av \Xv| (\Xv^\top \Av \Xv)^{-1} \Xv^\top \Av \\
    & = |\Xv^\top \Av \Xv| ((\Xv^\top \Av^\top \Xv)^{-1} \Xv^\top \Av^\top + (\Xv^\top \Av \Xv)^{-1} \Xv^\top \Av)
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 行列式对矩阵求导

如果$\Av$对称，则

$$
\begin{align*}
    \frac{\partial |\Xv^\top \Av \Xv|}{\partial \Xv} = 2 |\Xv^\top \Av \Xv| (\Xv^\top \Av \Xv)^{-1} \Xv^\top \Av
\end{align*}
$$

若$\Xv$、$\Av$是方阵，则其均可逆，于是

$$
\begin{align*}
    \frac{\partial |\Xv^\top \Av \Xv|}{\partial \Xv} = 2 |\Xv^\top| |\Av| |\Xv| \Xv^{-1} \Av^{-1} \Xv^{-\top} \Xv^\top \Av = 2 |\Xv|^2 |\Av| \Xv^{-1}
\end{align*}
$$

若$\Av = \Iv$，则

$$
\begin{align*}
    \frac{\partial |\Xv^\top \Xv|}{\partial \Xv} & = 2 |\Xv^\top \Xv| (\Xv^\top \Xv)^{-1} \Xv^\top = 2 |\Xv^\top \Xv| \Xv^\dagger \\
    \frac{\partial \ln |\Xv^\top \Xv|}{\partial \Xv} & = \frac{1}{|\Xv^\top \Xv|} \frac{\partial |\Xv^\top \Xv|}{\partial \Xv} = 2 \Xv^\dagger
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn
