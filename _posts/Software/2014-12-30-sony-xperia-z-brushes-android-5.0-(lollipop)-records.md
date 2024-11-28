---
title: Sony Xperia Z刷Android 5.0 (Lollipop)记录

categories:
  - 软件学习
translate_title: sony-xperia-z-brushes-android-5.0-(lollipop)-records
date: 2014-12-30 13:31:16
tags: [软件, 刷机, Android, Gapps]
---

周末闲来无事将手机（Sony Xperia Z）升级到了Android 5.0。该型号手机是包含在官方支持的升级到Android 5.0的列表里面的，不过真心的懒得一直等下去了，另外官方版一贯的预装一堆用不到的应用，既然等也是白等，所以还是提前动手了。

刷机包下载自[这里](https://www.blinkenlights.ch/ccms/android/yuga-l.html)。需要用的的主要是pabx_aosp_yuga-507.zip和gapps_50_yuga_004-00cb.tgz这两个包。需要用到的Flashtool工具下载自[这里](https://www.flashtool.net/downloads.php)。安装Flashtool后，将此前下载的pabx_aosp_yuga-507.zip包解压缩，然后将里面boot.img、system.img、userdata.img三个文件连同gapps_50_yuga_004-00cb.tgz一并拷贝到Flashtool安装路径下的x10flasher_lib目录，后续将这三个img文件直接烧录即可。

手机关机，按住“音量+”键数据线连接电脑，如果此前没有安装驱动，这时候会自动安装驱动，手机蓝灯模式。在x10flasher_lib文件夹在空白处，按住Shift键单击鼠标右键选择“在此处打开命令窗口”运行命令提示符（或者运行cmd，然后cd到该目录即可）。执行以下命令：
```shell 
fastboot flash boot boot.img
fastboot flash system system.img
fastboot flash userdata userdata.img
fastboot reboot
```
手机重启，不出意外的话已经进入Android 5.0界面。如果不需要Google应用程序套件，到此就可以停止了，需要的话，手机USB调试模式连接手机，默认其实已经打开，如果没有，请在设置-关于手机下面连续点击版本号，打开开发者模式，然后启用USB调试。
继续在x10flasher_lib文件夹下运行命令提示符，输入以下命令：

```shell
adb push gapps_50_yuga_004-00cb.tgz /sdcard/
adb reboot
```

手机重启，然后会自动安装Gapps套件。我这里没有使用原作者提供的Gapps的包，而是直接使用的此前已经精简过的版本，因为是用于Android 4.4.4的，这里就不再提供了。安装后是会自动升级的，所以其实版本影响不大。需要的可以自行寻找，一般是Zip包。安装步骤是将zip包拷贝到手机SD卡，然后手机重启，电源开始后猛按“音量-”键，进入recovery模式，然后选择从外部SD卡安装zip。安装结束后重启手机就可以了。

原作者提供的boot已经是可Root的版本，为了更好的管理Root权限，安装SuperSU。到[这里](https://download.chainfire.eu/624/SuperSU/BETA-SuperSU-v2.23.zip)下载，将其拷贝到SD卡，然后重启手机到Recovery模式，刷入即可。

删除系统预置程序，虽然安装的已经是原生版本（AOSP），不过还是有些程序是用不到的，或者有其他的理想替换，而自己又不想预置程序放在那里碍眼。我这里安装后预置的Email程序可以配置帐号，但是同步邮件的时候一直卡在那里。浏览器我一直用Chrome，另外预置的相机功能确实一般，所以需要将上述三个预置的应用删除。删除预置程序很简单，小心确认操作即可，同我们安装Gapps的过程，用到的依然是adb。
列表显示预置应用程序，一般是在system/app目录下：

```shell
adb shell ls /system/app
```
找到自己需要删除的内置程序，我这里是Email、Browser和Camera2这三个文件夹，早期版本直接是三个Apk文件，现在三个文件夹，子目录下才是对应的apk文件。接下来删除之：
首先挂载系统的读写权限：

```shell
adb remount
```
然后执行删除命令：

```shell
adb shell rm -R /system/app/Email
adb shell rm -R /system/app/Browser
adb shell rm -R /system/app/Camera2
```

