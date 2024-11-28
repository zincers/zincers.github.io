---
title: Tecplot如何导出Texted格式数据
id: 1297
categories:
  - 软件学习
translate_title: how-tecplot-exports-texted-format-data
date: 2016-08-10 21:02:11
tags: [CAE, Tecplot, 仿真, 后处理]
---

在Tecplot安装目录下找到tecplot.add，用文本编辑器打开。找到其中的如下行：

```yaml
# $!LoadAddon "excsv";        # Export data delimited by commas, spaces or tabs
```

删除前面的注释，激活该附加功能，然后在Tool菜单下面，就可以找到新激活的功能了。

注意如果是Cell-centered格式数据，目前还不支持该功能，需要首先将其转换为Nodal格式。

**Cell-centered格式转换为Nodal格式**

Tecplot可以基于cell-centered数据得到Nodal格式数据。假如我们需要得到节点格式的温度T_Node数据，而求解器默认输出的是cell-centered格式的温度T。转换方式如下：

1. 依次点击Data &gt; Alter &gt; Specify equations

2. 输入方程：{T_Node} = {T} 

3. 执行计算前设置新的变量位置为“Node”  

新得到的T_Node就是我们需要的格式，可以直接导出为csv格式的纯文本数据