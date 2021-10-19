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

GNN-HEADER 小结

正则化项 + 损失函数：

$$
\begin{align*}
    \min_\wv ~ \lambda \cdot \Omega(\wv) + \frac{1}{m} \sum_{i \in [m]} l(y_i, f(\xv_i))
\end{align*}
$$

<div class="threelines column1-border-right-solid head-highlight-1 tr-hover top-4 bottom-2">

|     模型     |   正则化项    |                    损失函数                     |          预测函数          |
| :----------: | :-----------: | :---------------------------------------------: | :------------------------: |
|   线性回归   |       -       |           $(\wv^\top \xv + b - y)^2$            |     $\wv^\top \xv + b$     |
|    岭回归    | $\|\wv\|_2^2$ |           $(\wv^\top \xv + b - y)^2$            |     $\wv^\top \xv + b$     |
|    LASSO     |  $\|\wv\|_1$  |             $(\wv^\top \xv - y)^2$              |       $\wv^\top \xv$       |
|    感知机    |       -       |        $\max \{ 0, - y \wv^\top \xv \}$         |    $\sgn(\wv^\top \xv)$    |
|  支持向量机  | $\|\wv\|_2^2$ |    $\max \{ 0, 1 - y (\wv^\top \xv + b) \}$     |  $\sgn(\wv^\top \xv + b)$  |
| 支持向量回归 | $\|\wv\|_2^2$ | $\max \{ 0, \wv^\top \xv + b - y - \epsilon \}$ |     $\wv^\top \xv + b$     |
| 对数几率回归 | $\|\wv\|_2^2$ |   $\log (1 + \exp (- y (\wv^\top \xv + b)))$    | $\sigma(\wv^\top \xv + b)$ |

</div>

### 以上线性模型均可通过引入核映射实现非线性预测能力

GNN-FOOTER 图神经网络导论 机器学习 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

GNN-HEADER 小结

GNN-FOOTER 图神经网络导论 机器学习 tengzhang@hust.edu.cn
