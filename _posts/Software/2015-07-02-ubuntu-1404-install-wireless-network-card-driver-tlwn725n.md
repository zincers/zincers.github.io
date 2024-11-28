---
title: Ubuntu 14.04安装无线网卡驱动TL-WN725N

categories:
  - 软件学习
translate_title: ubuntu-1404-install-wireless-network-card-driver-tlwn725n
date: 2015-07-02 18:06:07
tags: [软件, Linux, 驱动]
---

TL-WN725N 默认是可以驱动的，不过信号非常弱，Google一遭后终于解决：

```shell
sudo apt-get install git
git clone https://github.com/lwfinger/rtl8188eu.git
sudo apt-get install dkms
sudo dkms add ./rtl8188eu
sudo dkms build 8188eu/1.0
sudo dkms install 8188eu/1.0
```

参考：[https://project.altservice.com/issues/408](https://project.altservice.com/issues/408)