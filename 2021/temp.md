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

GNN-HEADER 链式法则

单变量求导中的<span class="blue">链式法则</span>为$\frac{\partial g(u)}{\partial x} = \frac{\partial g(u)}{\partial u} \frac{\partial u}{\partial x}$

情形一，只涉及向量：设$\xv \in \Rbb^n$，$\uv = \uv(\xv) \in \Rbb^m$，$\gv: \Rbb^m \mapsto \Rbb^l$，则

$$
\begin{align*}
    \underbrace{\frac{\partial \gv(\uv)}{\partial \xv}}_{l \times n} = \underbrace{\frac{\partial \gv(\uv)}{\partial \uv}}_{l \times m} \underbrace{\frac{\partial \uv}{\partial \xv}}_{m \times n}
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
    \frac{\partial g(u)}{\partial \Xv} = \frac{\partial g(u)}{\partial u} \frac{\partial u}{\partial \Xv}
\end{align*}
$$

这是因为

$$
\begin{align*}
    \left[ \frac{\partial g(u)}{\partial \Xv} \right]_{ij} & = \frac{\partial g(u)}{\partial x_{ji}} = \frac{\partial g(u)}{\partial u} \frac{\partial u}{\partial x_{ji}} = \frac{\partial g(u)}{\partial u} \left[ \frac{\partial u}{\partial \Xv} \right]_{ij}
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn
