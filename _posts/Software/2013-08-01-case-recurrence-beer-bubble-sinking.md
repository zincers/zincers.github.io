---
title: '案例复现:啤酒气泡下沉'

categories:
  - 软件学习
translate_title: case-recurrence-beer-bubble-sinking
date: 2013-08-01 16:39:08
tags: [CAE, COMSOL, 仿真, CFD, 计算, 气泡流, 多物理]
---

闲着逛果壳网，发现了这样一篇有意思的文章——《[啤酒泡泡物理学：气泡为何往下沉？](https://www.guokr.com/article/268900/)》，于是借助于COMSOL气泡流应用模式复现了一下该模型。背景介绍请参阅果壳网的链接，相关工作请查看老外的[项目介绍主页](https://www3.ul.ie/wlee/stout_beer.html)。不得不说，这些人真是无聊有趣的可以！

与模拟相关的部分主要是说杯子的形状对气泡沉浮影响显著，敞口的杯子倒入啤酒更容易形成逆天的下沉气泡。随附的模型是敞口杯的计算结果，如果想知道啤酒气泡在逐渐收紧的玻璃杯中会发生什么，替换一下玻璃杯的几何模型就可以了。当然，一个比较偷懒的做法是把体积力（重力）方向设定为垂直向上的，然后对应修改一下压力初始值。

![](/assets/img/blogimgs/cax/beer-bubble-sink.gif)

附件：[模型文件及相关资料](/assets/img/blogimgs/cax/beer-bubble-sink.zip)（模型版本COMSOL4.3b）

