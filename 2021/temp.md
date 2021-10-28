---
presentation:
  transition: "none"
  enableSpeakerNotes: true
  margin: 0
---

@import "../common/css/font-awesome-4.7.0/css/font-awesome.css"
@import "../common/css/zhangt-solarized.css"
@import "css/GNN.css"

<!-- slide data-notes="灵材：可免费获取的 MNIST 有 10 类，ImageNet 则有上千类，丹师是从药童做起，多模态：混合灵草和妖兽 <br><br> 丹方里最重要的是灵阵，控制如何抽取和凝结灵材中的灵性。灵阵中有若干节点，然后通过回路连接这些节点。灵材沿着回路游走经过每个节点处进行一步一步的提纯 <br><br> 半自动 不用你手动求导 做反向传播 更高端的可以使用多个丹炉同时开火炼制一枚灵丹 tf boy pt boy <br><br> 手中富裕的买 囊中羞涩的租" -->

GNN-HEADER 总结 当代炼丹术

```dot
digraph g {
    graph [nodesep=0.2, ranksep=0.4]
    rankdir=LR
    node [shape=plaintext color="#586e75" fontname="EBG,fzlz" fontcolor="#b58900" fontsize=18]
    edge [arrowhead=vee color="#586e75" fontname="EBG,fzlz" fontcolor="#268bd2" fontsize=14 arrowsize=0.5]
    bgcolor="transparent"

    subgraph cluster_1 {
        color="#586e75"
        fontcolor="#586e75"
        style="dashed"
        fontname="EBG,fzlz"
        label="增强品质"

        灵材

        node [fontcolor="#268bd2"]

        空间属性 时间属性 图属性
    }

    subgraph cluster_2 {
        color="#586e75"
        fontcolor="#586e75"
        style="dashed"
        fontname="EBG,fzlz"
        label="设计灵阵"

        丹方

        node [fontcolor="#268bd2"]

        卷积类 循环类 图类
    }

    subgraph cluster_3 {
        color="#586e75"
        fontcolor="#586e75"
        style="dashed"
        fontname="EBG,fzlz"
        label="精通用法"

        丹炉

        node [fontcolor="#268bd2"]

        半自动炼制 TensorFlow PyTorch
    }

    subgraph cluster_4 {
        color="#586e75"
        fontcolor="#586e75"
        style="dashed"
        fontname="EBG,fzlz"
        label="氪金"

        真火

        node [fontcolor="#268bd2"]

        炼制速度 "售 核弹厂" "租 阿里云"
    }

    subgraph cluster_5 {
        color="#586e75"
        fontcolor="#586e75"
        style="dashed"
        fontname="EBG,fzlz"
        label="控制调节"

        炼制

        node [fontcolor="#268bd2"]

        批量大小 随机丢弃 提早停止
    }

    灵材 -> 丹方 -> 丹炉 -> 真火 -> 炼制
}
```

一个优秀丹师的自我修养：

- 灵材品质差要会手动增强，旋转、翻转、缩放、平移、加噪声、标记平滑
- 因材制宜设计灵阵，空间属性灵材用卷积类灵阵，时间属性灵材用循环类...
- 仔细观察丹炉状态，防止爆炉，若最终仙丹成色不好则改进配置重新来过

GNN-FOOTER 图神经网络导论 神经网络 tengzhang@hust.edu.cn
