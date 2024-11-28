---
title: Ubuntu20.04下编译安装Elmer和ElmerGUI

categories:
  - 软件学习

translate_title: compile-and-install-Elmer-and-ElmerGUI-under-Ubuntu-20.04

date: 2021-08-19 19:10:49

tags: [CAE, Elmer, 仿真, 多物理, 计算, 开源, Linux]

---

安装依赖：

```shell
sudo apt install build-essential \
    git \
    libblas-dev \
    liblapack-dev \
    libmumps-dev \
    libparmetis-dev \
    libhypre-dev \
    gfortran \
    mpich \
    sudo \
    cmake \
    ca-certificates \
    less 
```

```shell
mkdir elmerfem
cd elmerfem
```

下载源码到 `repo`目录

```shell
git clone https://github.com/ElmerCSC/elmerfem.git repo
```


创建编译目录`build`并进入

```shell
mkdir build
cd build
```

#### 编译Elmer:

```shell
#Without MPI:
cmake -DCMAKE_INSTALL_PREFIX=/path/to/inst ../repo

#With MPI:
cmake -DWITH_OpenMP=TRUE -DWITH_MPI=TRUE -DCMAKE_INSTALL_PREFIX=/path/to/inst ../repo

make
make install
```

其中`/path/to/inst`是软件的安装目录，下同

#### 编译ElmerGUI：

软件默认使用的还是`QT4`，在 Ubuntu 20.04 的源中已经移除了`QT4`相关包，因此换用`QT5`，首先安装如下依赖：

```shell
#With ElmerGUI,USE QT4
#sudo apt install libqt4-dev libqwt-dev
#With ElmerGUI,USE QT5
sudo apt install liboce-modeling-dev \
	liboce-foundation-dev \
	qtscript5-dev \
	libqt5script5 \
	libqt5widgets5 \
	libqt5core5a \
	libqt5gui5 \
	libqt5help5 \
	libqt5opengl5 \
	libqt5opengl5-dev \
	libqt5svg5-dev \
	libvtk6.3 \
	libvtk6-dev \
	libvtk6.3-qt \
	libvtk6-qt-dev 
```

新建配置文件 `elmer.cmake`

````
vim ../elmer.cmake
````

输入如下内容：

```cmake
SET(WITH_MPI TRUE CACHE BOOL "")
SET(WITH_LUA TRUE CACHE BOOL "")
SET(CMAKE_BUILD_TYPE "RelWithDebInfo" CACHE STRING "")
SET(WITH_Mumps TRUE CACHE BOOL "")
SET(WITH_Hypre TRUE CACHE BOOL "")
SET(Hypre_INCLUDE_DIR "/usr/include/hypre" CACHE PATH "")
SET(WITH_ElmerIce TRUE CACHE BOOL "")

SET(ELMER_SOLVER_HOME "/usr/share/elmersolver" CACHE PATH "")

# ElmerGUI related.
SET(WITH_ELMERGUI TRUE CACHE BOOL "")
SET(WITH_OCC TRUE CACHE BOOL "")
SET(WITH_VTK FALSE CACHE BOOL "")
SET(WITH_PARAVIEW TRUE CACHE BOOL "")
SET(WITH_QWT FALSE CACHE BOOL "")
SET(WITH_QT5 TRUE CACHE BOOL "")
SET(QWT_LIBRARY "/usr/lib/libqwt-qt5.so.6" CACHE FILE "qwt library file name")
```

其中`WITH_ElmerIce`控制 `ElmerICE`模块编译，`WITH_QT5`使用`QT5`生成界面，`QWT_LIBRARY`用于手动指定依赖库。

最后，执行编译安装：

```shell
cmake -C ../elmer.cmake -DCMAKE_INSTALL_PREFIX=/path/to/inst ../repo
make
make install
```

#### 运行ElmerGUI：

使用完成路径启动 ElmerGUI

```shell
/path/to/inst/bin/ElmerGUI
```

如有必要，可以将`/path/to/dist/bin`加入到系统`PATH`变量，之后可以直接使用 `ElmerGUI`命令启动软件

#### Ref：

https://github.com/ElmerCSC/elmerfem

https://www.youtube.com/watch?v=OZ2Lvk-hEkc&ab_channel=elmerfem

