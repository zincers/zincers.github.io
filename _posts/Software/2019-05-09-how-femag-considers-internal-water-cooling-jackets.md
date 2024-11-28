---
title: FEMAG如何考虑内部水冷套
categories:
  - 软件学习
translate_title: how-femag-considers-internal-water-cooling-jackets
date: 2019-05-09 16:16:16
tags: [CAE, FEMAG, 仿真, CFD, 计算]
---

晶体生长热场模拟，如果设备包含内部水冷管（套）组件的时候，需要将内部边界等效为外部边界，从而指定其边界条件。在FEMAG软件中，设置方式如下：

1. 首先在 *GeoTool* 中，运行 *FurGeo* 进入炉子几何编辑。

2. 创建水冷组件几何，以及较小一点的内部水域几何，二者的差集（管壁）是我们需要的区域， *FurGeo* 并没有布尔运算功能，不能通过差集操作直接得到管壁特征，需要借助于辅助线来完成。

3. 如下图所示，以创建一个水冷管为例，借助于162和163两条线段，将管壁特征切分为如下三个区域，其中区域1和2是我们需要保留的管壁区域，区域3对应的则是水流流经的区域。

   ![FEMAG设置内部水冷示意图](/assets/img/blogimgs/cax/FEMAG_cap1.PNG)

4. 单击 *Create topology* 按钮，然后顺次点击 *Detect 2D* 和 *Detect 1D* 按钮，软件将自动检测和标记宏单元。 

5. 这之后，我们会发现区域3也被选中标记，需要我们手动取消标记。选中该区域，右键单击，然后选择 *Unassign* 选项即可。

6. 运行 *IniMesh* 和 *SetMesh* 组装几何和剖分网格。需要说明的是，在 *SetMesh* 过程中，一定不要将区域3误标记为gas宏单元。

7. 运行 *wxCregeo*。在 *Plot/Tree View* 窗口右侧的单元树中选择区域3对应的宏单元，右键菜单下单击 *Convert to external boundary* 选项。

8. 回到 *wxCregeo* 主窗口，在 *Thermal Operating Conditions* 选项面板中单击 *External boundary conditions (shell cooling, etc)* 右侧的 *Impose...* 按钮。

9. 经过如上设置，在弹出的对话框中，可以找到水冷套管内壁对应的边，这些边和炉体外壁一样，可以对其设置任意外部边界条件。

