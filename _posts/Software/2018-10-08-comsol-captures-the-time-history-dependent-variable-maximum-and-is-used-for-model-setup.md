---
title: COMSOL捕捉时间历程因变量最大值并用于模型设置
categories:
  - 软件学习
mathjax: true
translate_title: >-
  comsol-captures-the-time-history-dependent-variable-maximum-and-is-used-for-model-setup
date: 2018-10-08 20:16:53
tags: [CAE, COMSOL, 仿真, 多物理, 计算, 相变]
---

#### 问题描述

在COMSOL中模拟激光加热316L不锈钢粉末过程。激光加热达到转变点后，粉末融化，从粉末状态转变为实体状态，后续即便温度降低到转变点以下，316L依然保持实体状态，不会恢复为此前粉末状态。316L不锈钢的热传导系数、比热容、密度等参数都与粉末和实体转变的状态相关。模拟过程中需要使用变量捕捉时间历程中节点的温度结果，只要曾经高于转变点温度，即认为发生相变，修改状态变量的数值，后续无论升温和降温对该状态变量都无影响。在此基础上，316L的热物参数设置为与该状态变量相关的函数，相关参数作为材料本构加载到模型中去以表征相转变对加热过程的影响。

#### 相变过程的模拟

在COMSOL中模拟相变过程中材料属性参数的转变，相关的资料很多，这里不详述。

对于常见的固液相变，一般是定义一个相分数变量 $\phi$ ，让其在固相状态下为0，液相状态下为1。写成如下形式：
$$
\phi=(T>T_m)
$$
然后热物性能参数（这里以热传导系数为例）写成与 $\phi$ 相关的表达式：
$$
k=k_s(1-\phi)+k_l\phi
$$

使用上述表达式可以很好的处理可逆的相变过程，对于本需求中，转变为实体状态后即便降温依然保持实体状态的情形则无法处理。如果材料是整体加热从粉末态转变为实体态，而我们又可以判断整体完成转变的时间 $t_f$ 的话，可以简单将上式修改为如下形式：
$$
k=(k_s(1-\phi)+k_l\phi)(t<t_f)+k_l(t>t_f)
$$
激光加热，尤其是移动热源的激光加热，升温转变过程和降温过程在求解域中会同时存在，不存在前述的 $t_f$ ，所以上述思路不可行。

#### 捕捉时间周期变量最大值

换个思路来说，这个问题涉及的逻辑其实很简单，直接将 $\phi$ 的定义做个修改即可，如下：
$$
\phi=(T_{max}>T_m)
$$
刚好是我们需要的逻辑，于是问题就变为了如何获取时间历程中节点温度最大值的问题。COMSOL中，获取特定时刻域内最大值很简单，**模型定义**下有专门的算子可以用，但是获取时间历程节点的最大值的算子只有在后处理时候才有，不满足我们的需求。

查阅COMSOL文档，有一个$timemax()$函数让人眼前一亮，简直是量身定做的函数，文档引用如下：

>**timemax and timemin**
>
>The timemax and timemin operators evaluate the maximum and minimum, respectively, of an expression over time. timemax(t1,t2,expr) finds the maximum of expr on the interval t1 ≤ t ≤ t2. The first two arguments must be real constants
>
>**The timemax and timemin operators can only be used during results evaluation, so you cannot use then when setting up the model.** 

于是将 $\phi$ 定义成了 $timemax(0,t,T)>T_m$ 测试，单独用于捕捉 $\phi$ 数值没问题，一旦将 $\phi$ 和 $k$ 建立联系，并用于材料设置，软件就直接报错。仔细看文档发现，这个函数还是只能在后处理过程中用，无法用于设置模型（见引用文档加粗部分）。

#### 另辟路径

看文档过程中，同时发现了一个有意思的函数 $prev(expr,i)$ ，用于获取前 $i$ 个时间步的表达式 $expr$ 的数值。于是想到可以基于此实现类似 $timemax()$ 的功能。每个时刻判断该时刻温度 $T$ 与前一时刻 $T\_{max}$ 的大小，然后返回最大值给 $T\_{max}$ 。

$$
T_{max}=max(prev(T_{max},1),T)
$$
思路上没有问题，使用 $prex()$ 函数需求将求解类型切换为**Time Discrete**求解器，按需切换即可。至于如何将上述表达式写入软件，最开始的尝试是将这个关系写入全局方程。打开**Advanced Physics Options**选项，在分析模式中右键选择**Global** - **Global equations**。在**Global equations**的输入窗口**Name**中定义 $T\_{max}$ 变量，表达式中写入 $T\_{max}-max(prev(T\_{max},1),T)$，初始值按实际情况设置。通过这种方式理论上实现了使用 $T\_{max}$ 变量对温度最大值的捕捉，不过意外的是，这种情况依然报错。

抱着最后一丝希望，索性直接添加了一个 **General Form PDE**与原有的物理模式建立耦合分析。模型设置中，除了 $f$ 项外，所有的参数都设置为0，令 $f$ 项为$T\_{max}-max(prev(T\_{max},1),T)$。该思路与 **Global equations**类似，不同的是，基于这种方式获取的 $T\_{max}$ 可以正常应用于模型，与之建立关系的 $\phi$ 和 $k$ 都可以正常使用，并直接作为材料属性参数加载到模型中去。

大功告成，最后放一个测试的结果动画。左侧区域初始温度低于相变点，右侧区域初始温度高于相变点，左边界是高于相变点温度的恒温边界，右边界是低于相变点温度的恒温边界。最终结果是左侧随时间升温发生相变，右侧降温，温度会逐渐低于相变点温度。图中上方是温度分布结果，下方是对应的热传导系数的结果，从下方的图可以看到，左侧热物性能参数随着相变界面变化而变化，实现了对瞬态相变界面的实时追踪，右侧虽然温度逐渐低于相变温度，但是热物性能维持此前的最大值状态保持不变。

![COMOSL TimeMax](/assets/img/blogimgs/cax/comsol_timemax.gif)



<style>
p{font-family: sans-serif; font-size: 12pt;}
</style>
