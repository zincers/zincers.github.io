---
title: 修复Grub引导（EFI模式）
id: 1291
categories:
  - 软件学习
translate_title: fix-grub-boot-efi-mode
date: 2016-04-13 20:02:13
tags: [软件, 系统, Grub, EFI, 引导]
---

安装系统到U盘，自动将原来的EFI引导替换了，导致原来的Windows 10/XUbuntu 14.04双系统中Ubuntu 无法正常引导，启动直接进入了Grub界面。参考[这篇文章](http://www.ibm.com/developerworks/cn/linux/l-GRUB2-features/)修复之，具体过程如下：

*   1.首先ls产看硬盘分区，找到Linux系统/boot所在分区

    ```shell
    grub>ls
    (hd0) (hd0,gpt9) (hd0,gpt8) (hd0,gpt7) (hd0,gpt6) (hd0,gpt5) (hd0,gpt4) (hd0,gpt3) (hd0,gpt2) (hd0,gpt1)
    grub>ls (hd0,gpt8)/boot/grub
    abi-3.13.0-24-generic         memtest86+.elf
    abi-3.13.0-83-generic         memtest86+_multiboot.bin
    config-3.13.0-24-generic      System.map-3.13.0-24-generic
    config-3.13.0-83-generic      System.map-3.13.0-83-generic
    efi                           vmlinuz-3.13.0-24-generic
    grub                          vmlinuz-3.13.0-24-generic.efi.signed
    initrd.img-3.13.0-24-generic  vmlinuz-3.13.0-83-generic
    initrd.img-3.13.0-83-generic  vmlinuz-3.13.0-83-generic.efi.signed
    ```

*   2.识别 GRUB 配置文件所在位置后，设置 prefix 和 root 环境变量，告诉 GRUB 在何处找到配置文件。这些变量分别识别 grub.cfg 所在的目录和它所在的分区：
    ```shell
    grub>set prefix=(hd0,gpt8)/boot/grub
    grub>set root=(hd0,gpt8)
    ```

*   3.加载 normal 模块并启动它来调出 GRUB 菜单：
    ```shell
    grub>insmod normal
    grub>normal
    ```

*   4.到这里就进入到熟悉的Grub引导界面了，选择进入Linux系统，接下来还需要更新引导使得设置永久生效，使用 grub-mkconfig，从 Linux 命令提示符生成一个新的grub.cfg 文件：
    ```shell
    grub-mkconfig -o /boot/grub/grub.cfg
    ```

*   5.将 GRUB 重新安装到硬盘上，我的与Windows boot manager一起都是在sda2分区：
    ```shell
    grub-install /dev/sda2
    ```

