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

GNN-HEADER 标量对矩阵求导

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

GNN-HEADER 标量对矩阵求导

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

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 标量对矩阵求导

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
    \frac{\partial \tr(\Av \Xv \Xv^\top)}{\partial \Xv} = \frac{\partial \tr(\Xv^\top \Av \Xv)}{\partial \Xv} = \frac{\partial \tr(\Xv \Xv^\top \Av)}{\partial \Xv} = \Xv^\top \Av + \Xv^\top \Av^\top = \Xv^\top (\Av + \Av^\top)
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn
