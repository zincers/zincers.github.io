---
title: Xubuntu 14.04 下编译安装开源多物理场FEM仿真软件Elmer
id: 1157
categories:
  - 软件学习
translate_title: >-
  compile-and-install-open-source-multiphysics-fem-simulation-software-elmer-under-xubuntu-1404
date: 2014-05-24 19:10:49
tags: [CAE, Elmer, 仿真, 多物理, 计算, 开源, Linux]
---

关于**Elmer**，请参考[官方网站](http://www.csc.fi/english/pages/elmer/index_html)，是一个开源的可用于多物理场计算的FEM程序。支持对电磁、流体、结构力学、传热等问题做仿真分析，并支持将上述物理场耦合在一起做求解计算。XUbuntu软件源中包含Elmer，不过版本已经很老旧，安装后几乎不忍多视。对这个软件包感兴趣又不愿意费时间编译的，可以考虑直接下载安装[CAELinux](http://www.caelinux.com/CMS/)系统（当前版本是CAELinux2013，基于XUbuntu 12.04），里面整合了绝大多数用于数值仿真计算的软件包，可以直接使用。废话不多说，接下来是在XUbuntu 14.04下编译软件的过程。

安装编译环境

```shell
sudo apt-get install gcc
sudo apt-get install g++
sudo apt-get install gfortran
```

安装**svn**版本控制工具

```shell
sudo apt-get install subversion
```

从源中获取最新版本的Elmer源代码，源文件大小300M+，连接的是国外的服务器，执行完这条命可以根据自己的网速情况，考虑是否打开一部电影打发时间。

```shell
svn checkout http://svn.code.sf.net/p/elmerfem/code/trunk elmerfem
```

创建安装目录，并赋予读写权限：

```shell
sudo mkdir /opt/elmer
sudo chmod +775 /opt/elmer
cd elmerfem
```

创建脚本文件compile.sh:

```sh
#!/bin/sh -f</span>
#the compiler (here the gcc 4.X suite)
export CC=gcc
export CXX=g++
export FC=gfortran
export F77=gfortran
#the compiler flags
export CFLAGS=""
export FCFLAGS=""
export F77FLAGS=""
export FFLAGS=""
#linking
export LDFLAGS=""
#paths</span>
export ELMER_HOME="/opt/elmer"
# modules
modules="matc umfpack mathlibs elmergrid meshgen2d eio hutiter fem post"
# configure and build
for m in $modules;
  do
  cd $m;
  ./configure --prefix=ELMER_HOME
  make clean
  make
  make install
  cd ..
  done
```

赋予脚本文件可执行权限，并执行脚本：

```shell 
chmod u+x compile.sh
./compile.sh
```

创建环境变量

```shell 
export ELMER_HOME="/opt/elmer"
export PATH=PATH:ELMER_HOME/bin
export LD_LIBRARY_PATH=LD_LIBRARY_PATH:ELMER_HOME/lib
```

下一步就是编译安装ElmerGUI，ElmerGUI编译依赖QT、QWT、VTK等，以后有时间再鼓捣了。

参考资料：[Compilation of Elmer on Linux](http://www.elmerfem.org/elmerwiki/index.php?title=Compilation_of_Elmer_on_Linux "Compilation_of_Elmer_on_Linux")