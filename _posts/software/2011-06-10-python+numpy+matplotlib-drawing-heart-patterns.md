---
title: Python+Numpy+Matplotlib绘制心形图案

categories:
  - 软件学习
translate_title: python+numpy+matplotlib-drawing-heart-patterns
date: 2011-06-10 21:04:31
tags: [软件, 开发, Python, Numpy, Matplotlib]
---

闲来无事鼓捣Python，都说Python和Numpy配合，再搭配Matplotlib之后完全可以替代Matlab，一时兴起姑且安装试用之。之前曾见到有人用Matlab绘制心形图案，于是这次也以此为目的进行测试。

源码来自于**[此](https://stackoverflow.com/questions/4680525/plotting-implicit-equations-in-3d)**,本人稍作修改，然后添加了3D心形的隐函数进来。

```python
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
def fn(x,y,z):
    return ((x**2) + 9*(y**2)/4 + (z**2) - 1)**3-(x**2)*(z**3)-9*(y**2)*(z**3)/80
bbox=(-1.2,1.2)
xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
A = np.linspace(xmin, xmax, 100)
B = np.linspace(xmin, xmax, 50)
A1,A2 = np.meshgrid(A,A)

for z in B:
    X,Y = A1,A2
    Z = fn(X,Y,z)
    cset = ax.contour(X, Y, Z+z, [z], zdir='z',colors='r')

for y in B:
    X,Z = A1,A2
    Y = fn(X,y,Z)
    cset = ax.contour(X, Y+y, Z, [y], zdir='y',colors='b')

for x in B:
    Y,Z = A1,A2
    X = fn(x,Y,Z)
    cset = ax.contour(X+x, Y, Z, [x], zdir='x',colors='g')

ax.set_zlim3d(zmin,zmax)
ax.set_xlim3d(xmin,xmax)
ax.set_ylim3d(ymin,ymax)

plt.show()
```
最后，上图：

![3D-Heart-Python](/assets/img/blogimgs/cax/heart.png)

 Update：我都快忘了Python是用空格来控制循环体结构的了。
