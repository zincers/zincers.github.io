---
title: 基于Trelis 处理stl网格并导出

categories:
  - 软件学习
translate_title: processing-the-stl-grid-based-on-trelis-and-exporting
date: 2017-03-01 18:11:35
tags: [CAE, Trelis, 网格, STL]
---

1. 默认导出的STL文件是不包含网格的，需要使用“mesh”选项启用

  ```shell
  export stl 'file.stl' mesh
  ```

2. 基于已经剖分得到的网格创建meshed-based几何，然后导出stl文件

  ```shell
  import stl *** merge
  surface 1 size auto factor 1
  surface 1 scheme TriMesh geometry approximation angle 15
  mesh surface 1
  disassociate mesh vol all
  delete vol all
  create mesh geometry tri all
  export stl 'file.stl' overwrite
  ```

