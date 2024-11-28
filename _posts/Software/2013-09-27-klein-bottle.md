---
title: 克莱因瓶

categories:
  - 软件学习
translate_title: klein-bottle
date: 2013-09-27 18:28:17
tags: [CAE, COMSOL, 多物理, 仿真, 计算]
---

双莫比乌斯环组成的克莱因瓶

参数化曲面：

```matlab
R=2；u=[0,2pi]；v=[0,2pi]
x(u,v)=cos(u)(R+cos(u/2)cos(v)-sin(u/2)sin(2v))
y(u,v)=sin(u)(R+cos(u/2)cos(v)-sin(u/2)sin(2v))
z(u,v)=sin(u/2)cos(v)+cos(u/2)sin(2*v)
```


![](/assets/img/blogimgs/cax/mobius_strip_klein_bottle.gif) 

几何模型中曲面无法完全闭合，不得不说，COMSOL几何建模精度实在是差强人意啊。