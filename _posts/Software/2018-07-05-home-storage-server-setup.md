---
title: 家用存储服务器搭建
categories:
  - 软件学习
translate_title: home-storage-server-setup
date: 2018-07-05 20:16:53
tags: [NAS, 存储, 软件, Samba, Syncthing, Linux]
---

**硬件购置**

主板（板载CPU）：淘宝，华擎 J3455-ITX mini-ITX主板 17*17 4核CPU 

Nas机箱：淘宝，4盘位热插拔存储服务器 迷你ITX铝面板机箱DIY机箱，含电源和风扇

内存条：笔记本拆机内存条，三星 4G DDR3L 1600MHz

硬盘

- 机械硬盘：3.5寸  5400 SATA3 机械硬盘，西数蓝盘和希捷酷鱼各一块，一块做数据盘，一块做备份盘，京东618
- 固态硬盘：东芝 TR200系列 240GB SATA3固态硬盘，用作系统盘，京东618

配件：

- SATA3 数据线 * 2，主板仅包含两根数据线
- 临时要用的鼠键套装
- 主板支持 DVI+VGA+HDMI 三种视频输出，准备临时接显示器的线



**系统安装**

硬件几乎是按照”黑群晖“配置的，不过考虑到主要是以”做成家用存储“的名义瞎折腾，与其折腾NAS，做RAID一劳永逸，还不如直接做成一台Linux服务器，后期还可以随便加私货进去。于是乎直接做了个Ubuntu的启动U盘，装了Ubuntu 18.04上去。

装系统的时候仅插入了固态硬盘，刚开始的时候选择的手动分区，不过进行到最后一步安装Grub引导的时候报错，后来索性让系统使用全盘自动分的区，顺利通过。

系统安装完成按照惯例执行一些例行的操作，包括软件源切换国内，系统更新，固定IP配置，OpenSSH服务器安装等，这里不再赘述。



**挂载机械硬盘**

1. 完成系统安装，然后插入两块3.5的机械硬盘，进入Ubuntu。

2. 使用`df -h`命令查看两块硬盘默认挂载位置，我的是`/dev/sdb1`和`/dev/sdc`

3. 在根目录下新建data和backup目录，并修改权限，其中data用作数据盘，面向局域网服务，backup用作备份盘，每隔一定时间镜像data数据

   ``` shell
   sudo mkdir /data /backup
   sudo chmod -R 775 /data /backup
   ```

4. 修改etc/fstab文件，添加如下信息，设置开机自动将两块盘挂载到指定位置

   ```shell
   /dev/sdb1       /data           ext4    defaults        1       2
   /dev/sdc        /backup         ext4    defaults        1       2
   ```



**搭建Samba服务器** 

Samba服务器配置选项很多，这里仅需要配置局域网单用户可访问data目录即可。配置步骤如下：

1. 首先是安装Samba服务器：

   ```shell
   sudo apt-get install samba
   ```

2. Samba使用自己的用户账号和秘密，默认保存在`/etc/samba/smbpasswd` 文件中，可以使用`smbpasswd`命令 创建新的用户：

   ```shell
   sudo smbpasswd -a username
   ```

   按照程序指引，设置新用户密码，完成账号添加。

3. 修改配置文件，设置data目录局域网可访问：

   ```shell
   sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.bak	  # 备份配置文件，以防万一
   sudo vim /etc/samba/smb.conf						# 使用VIM编辑配置文件
   ```

   转到Samba长长的配置文件末尾，添加如下信息：

   ```reStructuredText
   [data]
   path = /data
   available = yes
   valid users = username
   read only = no
   browseable = yes
   public = yes
   writable = yes
   ```

4. 重启Samba服务器，使配置生效

   ```shell
   sudo /etc/init.d/smbd restart
   ```

5. Samba服务器重启后，使用如下命令测试配置文件是否有语法错误：

   ```shell
   sudo testparm
   ```

6. 至此，单用户的Samba服务器就搭建完成了，在局域网下应该可以浏览到该目录了。



**局域网其他设备访问Samba服务器**

- Windows：打开资源管理器，地址栏输入`\\192.168.2.200\data`即可浏览到共享的目录，其中192.168.2.200是Samba服务器内网IP。
- 手机：需求仅限于看服务器中视频资源的话，安装VLC视频播放器即可。需要浏览更多资源的话，可以安装类似于ES文件浏览器的应用。
- 电视机：家用的海信电视默认不支持Samba，需要安装第三方程序，比如小白文件管理器来支持。顺便分享一个海信官网的用户吐槽：[都什么年代了，居然还不支持Samba。。。](http://fans.hisense.com/thread-139650-1-1.html)



**手机相册同步**

相册同步使用的是[Syncthing](https://github.com/syncthing/syncthing)，Syncthing是开源的Resilio Sync 替代，支持在设备间进行文件的同步。

服务器端，下载最新版本的安装包，解压缩，然后运行解压缩目录下的`syncthing`即可：

```shell
wget https://github.com/syncthing/syncthing/releases/download/v0.14.48/syncthing-linux-amd64-v0.14.48.tar.gz
tar xvzf syncthing-linux-amd64-v0.14.48.tar.gz
cd syncthing-linux-amd64-v0.14.48
./syncthing
```

程序会自动启动Web界面，用于用户管理设备之间的同步。建议将`~/syncthing`加入到开机启动项中去。

Android手机自行搜索客户端下载安装即可，IOS目前还没有项目官方直接支持的客户端版本，商店里面的fsync()支持syncthing，不过没有具体测试过。文件夹同步设置按照客户端和服务器Web端引导设置即可。



**本机备份**

作为影音资源存储服务器，数据更新不会太频繁，实时同步意义不大，定期做一次归档就足够了。我这里使用第二块硬盘用于定期同步备份，相对于多盘配置RAID来说，这样确实简单粗暴了些，不过好处就是一旦data硬盘故障，直接把备份盘换过去即可。

定期备份使用rsync同步工具配合任务计划工具crontab实现。以设置每周日23点自动同步一次文件夹为例，配置过程如下，打开终端，执行：

```shell
crontab -e
```

编辑*crontab*文件，添加如下内容：

```shell
0 23 * * 0 rsync -az --delete --exclude 'lost+found' /data/ /backup/
```

Crontab参数说明：

```
*     *     *   *    *        command to be executed
-     -     -   -    -
|     |     |   |    |
|     |     |   |    +----- day of week (0 - 6) (Sunday=0)
|     |     |   +------- month (1 - 12)
|     |     +--------- day of        month (1 - 31)
|     +----------- hour (0 - 23)
+------------- min (0 - 59)
```

Rsync参数说明：

```shell
-a：归档模式，表示以递归方式传输文件，并保持所有文件属性，等于-rlptgoD
-z：对备份的文件在传输时进行压缩处理
--delete：删除目标路径下多余的文件；实现的效果其实是文件在原目录被删除，同步的时候也会删除目标目录的副本
--exclude：排除特定的目录和文件
```

同步命令`rsync`默认是将源目录同步到目标目录的同名子目录，data目录后面加`/`则直接同步data目录的所有子目录。



**下载工具推荐**

GUI：[webtorrent](https://webtorrent.io/)

CLI：[aria2](https://aria2.github.io/)

Aria2可以配置web前端，实现远程访问和管理。我这里偷懒没有配置，而是直接使用`nohup`配合`aria2`命令行实现远程下载，命令格式如下：

```shell
nohup [aria2下载命令] >out.log 2>&1 &
```


