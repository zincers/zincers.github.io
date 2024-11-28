---
title: MBD-Recursive Gimbal

categories:
  - 软件学习
translate_title: mbdrecursive-gimbal
date: 2013-11-11 18:52:25
tags: [CAE, 多物理, 仿真, MBD, 计算]
---

周末逛G+，无意中看到了这张图片，递归万向节（Recursive Gimbal），一时兴起决定借助COMSOL软件做一个测试模型。

![](/assets/img/blogimgs/cax/mbd_rotate/MBD_image.gif)

模型基于COMSOL Multiphysics平台的多体动力学模块（MBD），因为只是测试，这里只是做了两个圆环。

内部圆环初始角速度为30[deg/s]的角速度，简便起见采用柱坐标系，设定截图如下：

![](/assets/img/blogimgs/cax/mbd_rotate/Cap1.PNG)

左图是考虑了重力影响的结果，右侧是没有考虑重力作用的结果图：

|   |   |
|---|---|
|![](/assets/img/blogimgs/cax/mbd_rotate/MBD_Model.gif)|![](/assets/img/blogimgs/cax//mbd_rotate/MBD_Model_NoGravity.gif)|