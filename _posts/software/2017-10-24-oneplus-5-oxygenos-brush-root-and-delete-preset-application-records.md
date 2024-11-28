---
title: OnePlus 5 OxygenOS 刷机root以及删除预置应用记录
categories:
  - 软件学习
translate_title: oneplus-5-oxygenos-brush-root-and-delete-preset-application-records
date: 2017-10-24 19:53:00
tags: [软件, 刷机, Oneplus]
---

手机预装的是HydrogenOS，由于还是习惯Android原生体验，所以果断刷OxygenOS。OnePlus的OxygenOS预装了谷歌全家桶，相当一部分是用不到的，root之后直接删除这些预置应用。开始之前，确认打开开发者模式，以USB调试模式连接电脑。

**准备**

- [Platform Tools](https://dl.google.com/android/repository/platform-tools-latest-windows.zip)
- [twrp-3.1.1-1-cheeseburger.img](https://dl.twrp.me/cheeseburger/twrp-3.1.1-1-cheeseburger.img.html)
- [SuperSU](https://s3-us-west-2.amazonaws.com/supersu/download/zip/SuperSU-v2.82-201705271822.zip)

**开始**

1. 解压缩 Platform Tools 包，打开命令行并进入到该解压缩目录

2. 手机USB调试模式连接电脑，然后重启到 fastboot 模式

   ```Powershell
   adb.exe reboot bootloader
   ```

3. 手机解锁，如果已经解锁，可以跳过该步骤

   ```Powershell
   fastboot.exe oem unlock
   ```

4. 将 twrp-3.1.1-1-cheeseburger.img 重命名为 twrp.img  放在 Platform Tools 解压缩目录，然后将其刷入手机

   ```Powershell
   fastboot.exe flash recovery twrp.img
   ```

5. 重启手机

   ```Powershell
   fastboot.exe reboot
   ```

6. 键入 fastboot.exe reboot 后手机会自动重启，Oneplus会尝试将用户自定义的recovery替换为系统默认的，为了避免自定义recovery被还原，键入命令后，按住音量+键，选择启动到Twrp。

7. 成功进入Twrp界面后，选择刷入SuperSu，预先将SuperSu压缩包拷贝到手机中，浏览选择该压缩包刷入即可。

8. 刷入SuperSu后，重启手机，然后使用adb附带的命令行工具，删除不需要的预装应用

   ```shell
   adb.exe shell
   su  #切换到root用户，第一次需要在手机界面确认给予adb shell需要的root权限
   mount -o rw,remount /system  #挂载system文件系统为可读写
   cd /system/app  #进入系统预装app目录
   ls  #查看该目录下对应的app
   rm -R Gmail2 Duo YouTube Music2 ***  #删除不需要的预装app 
   ```

