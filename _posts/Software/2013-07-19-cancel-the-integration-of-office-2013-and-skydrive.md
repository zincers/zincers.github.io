---
title: 取消Office 2013与SkyDrive的整合
id: 1081
categories:
  - 软件学习
translate_title: cancel-the-integration-of-office-2013-and-skydrive
date: 2013-07-19 16:22:57
tags: [软件, Office, Onedrive]
---

无聊地将Office升级到了2013版本，然后发现用新版Office打开SkyDrive目录下的Office文档将会无比地悲剧。具体来说，因为新版Office和Microsoft的SkyDrive结合的更紧密，软件在打开SkyDrive目录下的文档的时候会自动查找云端的文档，以实现和云端的实时同步，当然基于此也可以实现多人协同编辑等高级功能。不过在网速不给力的时候，这项新技术显得无比的鸡肋。比如我在打开文档的时候，一直卡在“正在连接到SkyDrive”页面，因为网络延迟的缘故，很久才能将文档打开。

![](/assets/img/blogimgs/Office_SkyDrive/Cap01.png)

![](/assets/img/blogimgs/Office_SkyDrive/Cap02.png)

而编辑完文档保存退出后，卡在“正在上载到SkyDrive”页面，文档迟迟不能正常关闭。很明显微软的这项功能就不是为我等天朝低速网民开发的，在这里顺便鄙视一下武汉电信私自限制上传带宽的无良行为，投诉过去还死活不承认动了手脚，一味推说是我加装路由的原因。

因为打开SkyDrive目录以外的文档一切正常，所以很快就确定了问题的症结所在，那么接下来就是想办法把这项功能禁用掉了。当时遍查了Offce 2013的设置选项，试图将与SkyDrive的实时同步禁用掉，可是找了半天没找到可勾选的选项。最后几经折腾，误打误撞才发现原来这个设置早就在SkyDrive里面了，只是我一直没有注意而已。具体来说就是在SkyDrive的设置里面，取消“使用Office快速同步文件并与他人同时使用文件”这一项的勾选。

![](/assets/img/blogimgs/Office_SkyDrive/Cap03.png)

OK，一切恢复正常。当然对于网速还说得过去或者说完全不联网的用户来说，这完全是多此一举，不过话说回来，不联网谁还用SkyDrive啊。话说Office 2013搭配的这项快速同步功能，也就是所谓的“部分文件上传和下载功能”，极大地减小了SkyDrive后台同步的带宽占用，具体参看[这篇文章](http://livesino.net/archives/4361.live)。不过说实话，我看后更想诅咒网络运营商了。