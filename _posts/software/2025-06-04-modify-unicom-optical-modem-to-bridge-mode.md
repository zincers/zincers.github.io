---
title: 联通光猫改桥接（辽宁）

categories:
  - 软件学习

translate_title: modify-unicom-optical-modem-to-bridge-mode


date: 2025-06-04 15:00:49

tags: [网络, 光猫]

---
#### 写在前面
- 目的：局域网下搭建的Gitea、Immich相册和Aria2下载服务需要外部访问。

- 设备信息如下，不同地区，不同型号光猫，改桥接步骤不一，若型号不同，以下仅作为参考。
	- 设备型号：ZXHN F657GV9
	- 硬件版本号：V9.0
	- 软件版本号：V9.2.0P1T2  

- 辽宁联通虽然没有一开始就默认屏蔽80和443端口（改桥接后，这两个端口短暂使用了大约一周），但是之后检测到流量还是会屏蔽，所以外网访问一开始还是配置端口号吧，省的后期再改。

#### 光猫调整过程

- 以普通用户身份登录光猫（用户名：user，密码：见光猫背面），记录以下信息：
	- 宽带账号和密码：记录账号即可，密码我这里是123456,后面如果不是可以打联通客服电话重置；
		![](/assets/img/blogimgs/modem/account.png)

	- VID：
		![](/assets/img/blogimgs/modem/vid.png)
	
	- LOID:
		![](/assets/img/blogimgs/modem/loid.png)

- 拔掉光纤，用取卡针长按光猫重置键（reset），长按过程中光猫全部指示灯会闪烁，大约15s后，指示灯停止闪烁后，可以松开重置键。


- 重置光猫之后，光猫超级管理员账号会恢复为默认账号和密码，我这里默认账号和密码都是“lnadmin”（此前一直尝试CUAdmin，结果辽宁这里用的是“lnadmin”）。通过网线连接光猫的任意LAN口，浏览器访问：http://192.168.2.1/cu.html （注意后面有“cu.html”）使用默认超管账号和密码登录光猫。

- 屏蔽联通远程管理：
	- 修改超级管理员密码：“设备管理”-“用户管理”，修改管理维护账号的密码为自己的密码；
	- 关闭远程推送配置：进入“设备管理”-“设备管理”，取消“强制推送配置”页面“启用”后面的勾选。
		![](/assets/img/blogimgs/modem/cu_config.png)

	- 关闭TR069连接：进入“基本配置”-“上行线路配置”，在“WAN连接”页面，取消“1_TR069_R_VID_N”连接下侧“使能”的勾选；
		![](/assets/img/blogimgs/modem/cu_tr069.png)

- 新建WAN连接：在“WAN连接”页面，新建连接：
	- 封装类型：PPPoE；
	- 连接模式“Bridge”；
	- IP协议：“IPv4/v6”；
	- VLAN 模式：切换为“改写（tag）”，下方VLAN ID 输入此前记录的VID；
	- 确保“使能”勾选；
	- 单击“创建”完成新的WAN连接的设置。
	![](/assets/img/blogimgs/modem/cu_wan.png)

- 进入“高级配置”-“LOID配置”界面，输入此前记录的LOID，密码留空即可。输入完成后，点击保存，不要点击“认证注册”。
	![](/assets/img/blogimgs/modem/cu_loid.png)

- 至此，完成光猫的全部设置。此时可以将光纤重新插回了。切记，在此之前不要插入光纤，否则联通会自动推送配置并更新超级管理员密码。

#### 路由器切换为拨号上网

路由器型号不一，步骤大同小异，下面简要说明过程。

使用路由器访问地址（一般是：http://192.168.1.1）登录路由器，在上网设置那里将上网方式从“DHCP”切换为“PPPoE”，下面输入此前记录的宽带账号，密码为“123456”。保存后路由器会自动尝试拨号，如果密码错误，则拨打联通客服电话重置密码。

#### Ref：

https://keuin.cc/blog/china-unicomm-epon-hack/

https://inkflow.cc/other/64.html

