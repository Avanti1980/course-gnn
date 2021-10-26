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

GNN-HEADER 求解参数

整个网络：$\xv = \av_0 \xrightarrow{\Wv_1,\bv_1} \zv_1 \xrightarrow{h_1} \av_1 \xrightarrow{\Wv_2,\bv_2} \cdots \xrightarrow{\Wv_L,\bv_L} \zv_L \xrightarrow{h_L} \av_L = \hat{\yv}$

<br>

损失$\Lcal (\yv, \hat{\yv})$的计算为<span class="blue">正向传播</span>

- 样本从输入层进入，经隐藏层逐层传播到最后输出层
- $\hat{\yv} = \av_L = h_L (\zv_L)$是对样本$\xv$的预测，据此计算$\Lcal (\yv, \hat{\yv}) = \Lcal (\yv, h_L (\zv_L))$

<br>

先看最后一层$\zv_L = \Wv_L ~ \av_{L-1} + \bv_L$，$\av_L = h_L (\zv_L)$，由<span class="blue">链式法则</span> (?) 有

$$
\begin{align*}
    \frac{\partial \Lcal (\yv, \hat{\yv})}{\partial \Wv_L} & = \frac{\partial \Lcal (\yv, \hat{\yv})}{\partial \zv_L} \frac{\partial \zv_L}{\partial \Wv_L} = \deltav_L^\top \frac{\partial \zv_L}{\partial \Wv_L} \\
    \frac{\partial \Lcal (\yv, \hat{\yv})}{\partial \bv_L} & = \frac{\partial \Lcal (\yv, \hat{\yv})}{\partial \zv_L} \frac{\partial \zv_L}{\partial \bv_L} = \deltav_L^\top \frac{\partial \zv_L}{\partial \bv_L}
\end{align*}
$$

其中$\deltav_L^\top = \partial \Lcal (\yv, \hat{\yv}) / \partial \zv_L \in \Rbb^{n_l}$为第$L$层的<span class="blue">误差项</span>，该项可直接求解

GNN-FOOTER 图神经网络导论 神经网络 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 求解参数 反向传播

整个网络：$\xv = \av_0 \xrightarrow{\Wv_1,\bv_1} \zv_1 \xrightarrow{h_1} \av_1 \xrightarrow{\Wv_2,\bv_2} \cdots \xrightarrow{\Wv_L,\bv_L} \zv_L \xrightarrow{h_L} \av_L = \hat{\yv}$

<br>

先看最后一层$\zv_L = \Wv_L ~ \av_{L-1} + \bv_L$，$\av_L = h_L (\zv_L)$，由<span class="blue">链式法则</span> (?) 有

$$
\begin{align*}
    \frac{\partial \Lcal (\yv, \hat{\yv})}{\partial \Wv_L} = \deltav_L^\top \frac{\partial \zv_L}{\partial \Wv_L}, \quad \frac{\partial \Lcal (\yv, \hat{\yv})}{\partial \bv_L} = \deltav_L^\top \frac{\partial \zv_L}{\partial \bv_L}
\end{align*}
$$

其中$\deltav_L^\top = \partial \Lcal (\yv, \hat{\yv}) / \partial \zv_L \in \Rbb^{n_l}$为第$L$层的<span class="blue">误差项</span>，该项可直接求解

<br>

误差<span class="blue">反向传播</span> (<u>b</u>ack<u>p</u>ropagation, BP)：前一层的误差可由后一层得到

$$
\begin{align*}
    \deltav_{l-1}^\top = \frac{\partial \Lcal (\yv, \hat{\yv})}{\partial \zv_{l-1}} = \frac{\partial \Lcal (\yv, \hat{\yv})}{\partial \zv_l} \frac{\partial \zv_l}{\partial \av_{l-1}} \frac{\partial \av_{l-1}}{\partial \zv_{l-1}} = \deltav_L^\top \frac{\partial \zv_l}{\partial \av_{l-1}} \frac{\partial h_{l-1}(\zv_{l-1})}{\partial \zv_{l-1}}
\end{align*}
$$

对第$l$层$\zv_l = \Wv_l ~ \av_{l-1} + \bv_l$，如何求$\partial \zv_l / \partial \Wv_l$、$\partial \zv_l / \partial \bv_l$、$\partial \zv_l / \partial \av_{l-1}$？

GNN-FOOTER 图神经网络导论 神经网络 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 求解参数 反向传播

对第$l$层$\zv_l = \Wv_l ~ \av_{l-1} + \bv_l$，如何求$\partial \zv_l / \partial \Wv_l$、$\partial \zv_l / \partial \bv_l$、$\partial \zv_l / \partial \av_{l-1}$？

由矩阵求导公式易知

$$
\begin{align*}
    \frac{\partial \zv_l}{\partial \bv_l} = \frac{\partial \bv_l}{\partial \bv_l} = \Iv, \quad \frac{\partial \zv_l}{\partial \av_{l-1}} = \frac{\partial (\Wv_l ~ \av_{l-1})}{\partial \av_{l-1}} = \Wv_l
\end{align*}
$$

GNN-FOOTER 图神经网络导论 神经网络 tengzhang@hust.edu.cn
