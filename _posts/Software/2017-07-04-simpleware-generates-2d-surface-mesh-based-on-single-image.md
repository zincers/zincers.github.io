---
title: Simpleware基于单张图像生成2D面网格
categories:
  - 软件学习
translate_title: simpleware-generates-2d-surface-mesh-based-on-single-image
date: 2017-07-04 20:16:53
tags: [CAE, Simpleware, 仿真, 网格, 计算, 3D重构]
---

Simpleware可以基于3D图像重构CAD模型并生成用于有限元和流体计算的网格，相关功能有很多讨论，这里不再赘述。

部分用户尤其是材料领域用户，限于实验条件，很多时候只有单张截面图（典型的，SEM照片），用户的需求也仅是处理2D的图像，然后得到2D面网格。如果使用Simpleware导入单张图片的话，软件默认是将其按照一个像素厚度的3D数据处理的，网格剖分之后默认导出的也是3D的网格，而且由于Z方向只有一个像素厚度（典型的薄层特征），所以网格质量也很差。想要规避Z方向的薄层特征，很容易想到的一个解决方案是将图片多复制几张，不过上述操作默认导出的依然是3D网格，导入到求解器之后只能通过在Z方向的上下两个面施加（周期）对称之类的边界条件，以便于基于3D网格近似处理2D问题。

上述方案将简单的2D问题复杂化成了3D问题，虽然思路上可行，但是显然会浪费大量的计算资源。事实上Simpleware本身是支持直接导出某个Shell面的2D网格的，只不过藏的比较深而已。接下来我们就来看一下相关的步骤：

逻辑上，Simpleware依然只能处理3D图像数据，所以第一步依然是将图片在Z方向复制（或者重复导入），复制的目的是为了后续图像平滑滤波等算法可以顺利使用，同时也是为了弱化薄层特征。一般而言建议复制五层以上。

平滑滤波、然后按照自己的需要分割图像，具体步骤这里不展开，这些都是Simpleware平台基础的功能，根据自己图像的特征灵活选择即可，得到自己想要Mask之后，选择创建FE模型。截至这里，流程上其实依然是2D问题转化为3D问题处理的思路。接下来的步骤则需要特别注意。

打开**Model configuration**窗口，切换到**Volume meshing**选项卡，点击**More options**展开高级设置，找到**Target number of elements across a layer**，然后将其值设置为0.01。

![](/assets/img/blogimgs/cax/simpleware/Simpleware_2d_mesh_cap1.png)

我们最终要的其实仅仅是垂直于Z方向的某一个面的面网格就可以了，所以Z方向上网格质量好坏是无所谓的，所以这里选择将薄层最小网格层数的参数设置为一个很小的值。

标记要导出的shell特征，选择垂直于Z方向的某一个面（这里以ZMax为例），Zmax和我们生成的Mask重合的区域就是我们最后要的特征，如果有多个Mask，需要分别标记。

![](/assets/img/blogimgs/cax/simpleware/Simpleware_2d_mesh_cap2.png)

这时候选择生成网格，得到的依然是3D网格，因为薄层参数的设置，Z方向网格质量没有限制，会比较粗糙，这刚好是我们期望的。直接将该3D网格导出不是我们的预期，在生成网格之前，有一个关键步骤就是选择所有的Mask，将其标记为non - export part。上述设置确保在导出的时候，只导出Shell特征，实体部分网格不再导出之列。

![](/assets/img/blogimgs/cax/simpleware/Simpleware_2d_mesh_cap3.png)

导出的网格直接用CAE软件打开会识别为shell特征。如果使用的CAE软件需要建模开始就选择维度，建议导出类型选择Nastran（.nas）格式。然后在CAE软件中创建2D模型，最后选择导入之前生成的.nas网格就可以了。

![](/assets/img/blogimgs/cax/simpleware/Simpleware_2d_mesh_cap4.png)

