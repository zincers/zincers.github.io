---
title: 编译安装elmer图形用户界面ElmerGUI

categories:
  - 软件学习
translate_title: compile-and-install-elmer-graphical-user-interface-elmergui
date: 2014-06-06 19:13:13
tags: [软件, CAE, 开发, 编译, Elmer, 多物理, GUI]
---

ElmerGUI需要qmake。
```shell
sudo apt-get install qt4-qmake</pre>
```
收敛曲线绘图依赖qwt
```shell
sudo apt-get install llibqwt5-qt4-dev
```
安装图形界面和后处理依赖的vtk库
```shell
sudo apt-get install libvtk5-dev
sudo apt-get install libvtk5-qt4-dev
```
安装其他依赖环境
```shell
sudo apt-get install libftgl2
sudo apt-get install libtbb2
sudo apt-get install libgl2ps0
sudo apt-get install libfreeimage3
sudo apt-get install libpythonqt2.1
```
转到源文件目录
```shell
cd elmerfem/ElmerGUI
```
打开并编辑配置文件ElmerGUI.pri。下面是修改之后的配置文件，因为我这里没有安装OpenCASCADE，所以可选组件这里注销掉了下面这一行。
```pri
#DEFINES += EG_OCC      # Use OpenCASCADE 6.3 for importing CAD files? Needs VTK.
```
```yaml
#############修改后的配置文件，开始#####################

#                       ElmerGUI: configuration file
#
#==============================================================================
#------------------------------------------------------------------------------
# Optional components (undefine or comment out to exclude from compilation):
#------------------------------------------------------------------------------
DEFINES += EG_QWT      # Use QWT for convergence monitor?
DEFINES += EG_VTK      # Use VTK for postprocessing?
DEFINES += EG_PARAVIEW # Use ParaView for postprocessing?
DEFINES += EG_MATC     # Use MATC for internal operations in postprocessing?
#DEFINES += EG_OCC      # Use OpenCASCADE 6.3 for importing CAD files? Needs VTK.
DEFINES -= EG_PYTHONQT # Use PythonQt for scripting in post processor?
#------------------------------------------------------------------------------
# 64 bit system?
#------------------------------------------------------------------------------
BITS = 64
#------------------------------------------------------------------------------
# Installation directory:
#------------------------------------------------------------------------------
ELMERGUI_HOME = $$(ELMERGUI_HOME)
isEmpty(ELMERGUI_HOME) {
ELMER_HOME = $$(ELMER_HOME)
isEmpty(ELMER_HOME) {
unix: ELMER_HOME = /opt/elmer
win32: ELMER_HOME = c:/Elmer7
macx: ELMER_HOME = /usr/local
}
ELMERGUI_HOME = $${ELMER_HOME}/bin
}
#------------------------------------------------------------------------------
# Python library:
#------------------------------------------------------------------------------
unix {
PY_INCLUDEPATH = /usr/include/python2.7
PY_LIBPATH = /usr/lib
PY_LIBS = -lpython2.7
}
win32 {
PY_INCLUDEPATH = c:/PYTHON/Python-2.6.1/Include
PY_LIBPATH = c:/PYTHON/Python-2.6.1/PCbuild
PY_LIBS = -lpython26
}
macx {
}
#------------------------------------------------------------------------------
# QWT library:
#------------------------------------------------------------------------------
unix {
QWT_INCLUDEPATH = /usr/include/qwt-qt4
QWT_LIBPATH = /usr/lib
QWT_LIBS = -lqwt-qt4
}
win32 {
QWT_INCLUDEPATH = c:/Source/Qwt/include
QWT_LIBPATH = c:/Source/Qwt/lib
QWT_LIBS = -lqwt5
}
macx {
QWT_INCLUDEPATH = /usr/local/qwt-5.0.2/include
QWT_LIBPATH = /usr/local/qwt-5.0.2/lib
QWT_LIBS =  -lqwt5
}
#------------------------------------------------------------------------------
# VTK library:
#------------------------------------------------------------------------------
unix {
VTK_INCLUDEPATH = /usr/include/vtk-5.8
VTK_LIBPATH = /usr/lib/vtk-5.8
VTK_LIBS = -lQVTK \
-lvtkCommon \
-lvtkDICOMParser \
-lvtkFiltering \
-lvtkGenericFiltering \
-lvtkGraphics \
-lvtkHybrid \
-lvtkIO \
-lvtkImaging \
-lvtkInfovis \
-lvtkNetCDF \
-lvtkRendering \
-lvtkViews \
-lvtkVolumeRendering \
-lvtkWidgets
}
win32 {
VTK_INCLUDEPATH = c:/Source/VTK/include/vtk-5.4
VTK_LIBPATH = c:/Source/VTK/lib/vtk-5.4
VTK_LIBS = -lQVTK \
-lvtkCommon \
-lvtkDICOMParser \
-lvtkFiltering \
-lvtkGenericFiltering \
-lvtkGraphics \
-lvtkHybrid \
-lvtkIO \
-lvtkImaging \
-lvtkInfovis \
-lvtkNetCDF \
-lvtkRendering \
-lvtkViews \
-lvtkVolumeRendering \
-lvtkWidgets \
-lvtkexoIIc \
-lvtkexpat \
-lvtkfreetype \
-lvtkftgl \
-lvtkjpeg \
-lvtklibxml2 \
-lvtkmetaio \
-lvtkpng \
-lvtksys \
-lvtktiff \
-lvtkverdict \
-lvtkzlib \
-ladvapi32
}
macx {
VTK_INCLUDEPATH = /usr/local/include/vtk-5.0
VTK_LIBPATH = /usr/lib
VTK_LIBS = -lvtkHybrid \
-lvtkWidgets \
-lQVTK
}
#------------------------------------------------------------------------------
# OpenCASCADE library:
#------------------------------------------------------------------------------
unix {
OCC_INCLUDEPATH = /usr/include/opencascade
OCC_LIBPATH = /usr/lib
OCC_LIBS = -lTKSTL \
-lTKBRep \
-lTKernel \
-lTKG2d \
-lTKG3d \
-lTKGeomAlgo \
-lTKGeomBase \
-lTKMath \
-lTKMesh \
-lTKShHealing \
-lTKSTEP \
-lTKSTEP209 \
-lTKSTEPAttr \
-lTKSTEPBase \
-lTKIGES \
-lTKTopAlgo \
-lTKXSBase
}
win32 {
OCC_INCLUDEPATH = $(CASROOT)/inc
OCC_LIBPATH = $(CASROOT)/win32/lib
OCC_LIBS = $(CASROOT)/win32/lib/TKBRep.lib \
$(CASROOT)/win32/lib/TKernel.lib \
$(CASROOT)/win32/lib/TKG2d.lib \
$(CASROOT)/win32/lib/TKG3d.lib \
$(CASROOT)/win32/lib/TKGeomAlgo.lib \
$(CASROOT)/win32/lib/TKGeomBase.lib \
$(CASROOT)/win32/lib/TKMath.lib \
$(CASROOT)/win32/lib/TKMesh.lib \
$(CASROOT)/win32/lib/TKShHealing.lib \
$(CASROOT)/win32/lib/TKSTEP.lib \
$(CASROOT)/win32/lib/TKSTEP209.lib \
$(CASROOT)/win32/lib/TKSTEPAttr.lib \
$(CASROOT)/win32/lib/TKSTEPBase.lib \
$(CASROOT)/win32/lib/TKIGES.lib \
$(CASROOT)/win32/lib/TKTopAlgo.lib \
$(CASROOT)/win32/lib/TKXSBase.lib
}
macx {
OCC_INCLUDEPATH =
OCC_LIBPATH =
OCC_LIBS =
}

#############修改后的配置文件，结束#####################
```

执行编译
```shell
qmake
make
```
执行编译之后报错，提示找不到qwt_compat.h，报错指向`/ElmerGUI/Application/src/convergenceview.h`文件，打开该文件，找到如下这两行
```c
/*include <qwt_data.h>; <-- deprecated in Qwt6, using qwt_compat.h instead*/
#include <qwt_compat.h>; 
```
将其修改为：
```c
#include <qwt_data.h> <-- deprecated in Qwt6, using qwt_compat.h instead
/*#include <qwt_compat.h>*/
```
继续执行编译
```shell
make
```
编译错误，报错指向`/ElmerGUI/Application/src/convergenceview.cpp`文件，打开该文件。找到如下行：
```cpp
double x = (double)(curve->d_data->count());
curve->d_data->append(&x, y, size);
/*curve->d_curve->setRawData(curve->d_data->x(),
			curve->d_data->y(),
			curve->d_data->count()); */
curve->d_curve->setRawSamples(curve->d_data->x(),
			curve->d_data->y(),
			curve->d_data->count());
plot->setTitle(title);
```
将其修改为如下所示，然后保存退出。
```cpp
double x = (double)(curve->d_data->count());
curve->d_data->append(&x, y, size);
curve->d_curve->setRawData(curve->d_data->x(),
			curve->d_data->y(),
			curve->d_data->count());
/*curve->d_curve->setRawSamples(curve->d_data->x(),
			curve->d_data->y(),
			curve->d_data->count());*/
plot->setTitle(title);
```
继续执行编译
```shell
make
```
编译器报错提示：
```shell
/usr/bin/ld: cannot find -lvtkNetCDF
```
这里需要安装libvtkNetCDF库，因为此前安装了paraview所以直接建立了一个链接：
```shell
sudo ln /usr/lib/paraview/libvtkNetCDF.so /usr/include/vtk-5.8/
```
再次执行编译，终于顺利完成，长嘘一口气！！！
```shell
make
```
最后编译安装：
```shell
make install
```
创建环境变量：
```shell
export ELMERGUI_HOME = $ELMER_HOME/bin
```
最后，上张图，算作对这两天折腾的总结吧。
![](/assets/img/blogimgs/cax/ElmerGUI.png)