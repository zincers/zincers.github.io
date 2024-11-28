---
title: Linux下批量转换avi文件为gif动画
id: 1155
categories:
  - 软件学习
translate_title: batch-convert-avi-file-to-gif-animation-under-linux
date: 2014-05-13 19:09:13
tags: [软件, Linux]
---

工作需要，有一堆avi格式的小视频需要批量转换为gif动画。相较于直接在幻灯片中插入avi格式的视频而言，gif格式的动画不需要额外的播放设置，更加的方便。因为文件比较多，在Windows找了半天，都没有找到一个可以批量处理的工具，于是自然而言想到转到Linux平台用ffmpeg来做。切换后发现，xubuntu 14.04下已经不包含ffmpeg的源，取而代之的是libav-tools。

```shell 
sudo apt-get install libav-tools
for it in *.avi
do
   avconv -i it -pix_fmt rgb24 -vframes 10 it.gif
done
```

*参数说明：*

```-pix_fmt```: 像素格式

```-vframes```: 动画帧数

