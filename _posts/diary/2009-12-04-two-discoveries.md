---
title: 两个发现

categories:
  - 日志随笔
translate_title: two-discoveries
date: 2009-12-04 10:59:00
tags:
---

今天msn突然无法登陆，调试了半天，尝试了各种办法均无济于事，因为上网环境是教育网，比较不稳定，所以前期以为是网络问题，甚至猜想可能是局域网路由器问题。确认网络连接之后，本能地去查找软件问题，为此重装了整个live套件。不过依旧不见效。这之后发现问题绝非我想象的那么简单，很明显的是，在别人的机器登陆我的帐号一样无法登陆，而在我的机器登陆别人的帐号却正常。

求助于Google，得到的结果是msn联系人中有不和谐的联系人。此后登陆web版msn删除了一大批可能的msn联系人，然后重试登陆，竟然恢复了。

在此过程中发现了以下两点：首先如上所说，msn联系人中存在敏感联系人会导致msn无法登陆，因为功夫网很好的伪装，在我们看来将是网络问题，当然事实上你的网络其实一点问题没有。另外，我使用的是msn的英文版，之前大家一致认为msn英文版不会被功夫网监控，但是由此似乎证明这条消息不确切。

现在想来，出现问题的联系人应该是twitteronmsn这个机器人，如你所知，这个机器人用来接收发送twitter上的消息。因为twitter上一贯的自由言说，使得这个机器人发送过来的消息中多有"不和谐"的字词，这可能是这个机器人遭殃的首因。因为这点发现还没有被广泛确认，所以这里我姑且不过多评论。不过有一点是确定无疑的，那就是功夫网真的已经做到了窥探我们msn联系人的地步，所谓的个人隐私，在贵国已经无从谈起。

在这里犹豫要不要转向gtalk，遗憾的是我的gtalk真的有些冷清。

**Update**：出现这种情况后，修改主机登陆msn的方法还是可行的！

Update 1：

已证实，添加twitteronmsn机器人的确可以导致msn无法登陆，功夫网终于盯上这个机器人了。解决方法为web方式登陆msn，然后忍痛删除该机器人；或者修改主机文件，在hosts文件中加入如下两行：
```powershell
65.54.239.80 messenger.hotmail.com
65.54.239.80 dp.msnmessenger.akadns.net  # 推荐使用后者。
```

[译言网](https://www.yeeyan.com/)宕机是因为维护还是被维护的猜测终于结束。事实证明绝非贵国人民敏感，以现在的技术条件，再大型的网站维护都不需要超过两给小时，如果超过两个小时，十有八九皆是被维护。在这个问题上，叽歪的表现绝对诚实，网站主页的那句被维护说得是那么的有趣。

央视昨天以搜索结果含色情链接为由向各大搜索引擎开炮，如你所知，这已经不是央视第一次干这种事情。感觉又快到年终了，央视不开炮以此来讨点钱花那还叫央视吗！今年的春晚会是谁来赞助？这个问题值得期待。