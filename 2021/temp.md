---
presentation:
  transition: "none"
  enableSpeakerNotes: true
  margin: 0
---

@import "../common/css/font-awesome-4.7.0/css/font-awesome.css"
@import "../common/css/zhangt-solarized.css"
@import "css/GNN.css"

<!-- slide data-notes="90 年代被美国很多银行用来识别支票上面的手写数字" -->

GNN-HEADER 经典网络 LeNet-5

<img src="../tikz/lenet.svg" class="center width75 top1 bottom1">

<div class="threelines lenet top-2 bottom-2">

| 层数 |             作用              |      神经元数量      |         参数个数          |
| :--: | :---------------------------: | :------------------: | :-----------------------: |
|  1   |            输入层             |   32 × 32 = 1,024    |             -             |
|  2   |  卷积层 6 个 5 × 5 的卷积核   | 6 × 28 × 28 = 4,704  |     6 × 25 + 6 = 156      |
|  3   |  平均汇聚层 采样窗口为 2 × 2  | 6 × 14 × 14 = 1,176  |             -             |
|  4   |  卷积层 60 个 5 × 5 的卷积核  | 16 × 10 × 10 = 1,600 |   60 × 25 + 16 = 1,516    |
|  5   |  平均汇聚层 采样窗口为 2 × 2  |   16 × 5 × 5 = 400   |             -             |
|  6   | 卷积层 1920 个 5 × 5 的卷积核 |   1920 / 16 = 120    | 1,920 × 25 + 120 = 48,120 |
|  7   |           全连接层            |          84          |  84 × (120 + 1) = 10,164  |
|  8   |    输出层 10 个径向基函数     |          -           |             -             |

</div>

GNN-FOOTER 图神经网络导论 卷积神经网络 tengzhang@hust.edu.cn
