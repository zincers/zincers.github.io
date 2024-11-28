---
title: 3D心形参数化曲线
id: 1077
categories:
  - 软件学习
translate_title: 3d-heart-shaped-parametric-curve
date: 2013-07-16 16:17:46
tags: [CAE, COMSOL, 仿真, 计算]
---

3D 心形参数化曲线：

```matlab
u(theta)=cos(theta)(sin(theta)sqrt(abs(cos(theta)))/(sin(theta)+7/5)-2sin(theta)+2)(theta(40pi-theta)); 
v(theta)=sin(theta)(sin(theta)sqrt(abs(cos(theta)))/(sin(theta)+7/5)-2sin(theta)+2)(theta(40pi-theta)); 
w(theta)=50*theta; 
theta =[0,40*pi]
```

效果见下图，基于COMSOL Multiphysics做的管道传热模型：

![](/assets/img/blogimgs/cax/3D-Heart.gif) 