---
presentation:
  transition: "none"
  enableSpeakerNotes: true
  margin: 0
---

@import "../common/css/font-awesome-4.7.0/css/font-awesome.css"
@import "../common/css/zhangt-solarized.css"
@import "css/GNN.css"

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 迹对矩阵求导

$$
\begin{align*}
    \left[ \frac{\partial \tr(\Uv \Vv)}{\partial \Xv} \right]_{ij} = \frac{\partial \tr(\Uv \Vv)}{\partial x_{ji}} = \tr \left( \frac{\partial (\Uv \Vv)}{\partial x_{ji}} \right)
\end{align*}
$$

取$\Uv = \Iv$，$\Vv = \Av \otimes \Xv, ~ \Xv \otimes \Xv$，则

$$
\begin{align*}
    & \left[ \frac{\partial \tr(\Av \otimes \Xv)}{\partial \Xv} \right]_{ij} = \tr \left( \frac{\partial \Av \otimes \Xv}{\partial x_{ji}} \right) = \tr \left( \Av \otimes \frac{\partial \Xv}{\partial x_{ji}} \right) \\
    & ~ = \tr ( \Av \otimes \Ev_{ji} ) = \tr(\Av) \delta_{ij} \Longrightarrow \frac{\partial \tr(\Av \otimes \Xv)}{\partial \Xv} = \tr(\Av) \Iv \\
    \\
    & \left[ \frac{\partial \tr(\Xv \otimes \Xv)}{\partial \Xv} \right]_{ij} = \tr \left( \frac{\partial \Xv \otimes \Xv}{\partial x_{ji}} \right) = \tr \left( \frac{\partial \Xv}{\partial x_{ji}} \otimes \Xv + \Xv \otimes \frac{\partial \Xv}{\partial x_{ji}} \right) \\
    & ~ = \tr ( \Ev_{ji} \otimes \Xv ) + \tr ( \Xv \otimes \Ev_{ji} ) = 2 \tr(\Xv) \delta_{ij} \Longrightarrow \frac{\partial \tr(\Xv \otimes \Xv)}{\partial \Xv} = 2 \tr(\Xv) \Iv
\end{align*}
$$

GNN-FOOTER 图神经网络导论 矩阵求导 tengzhang@hust.edu.cn
