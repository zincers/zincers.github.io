---
title: 钉钉机器人自动推送外网IP到群组
categories:
  - 软件学习
translate_title: nail-robot-automatically-pushes-external-network-ip-to-group
date: 2017-09-04 20:16:53
tags: [软件, Python, 开发, 网络, 钉钉, IP]
---

工作需要，在局域网内搭建了Gitlab服务器，然后借助花生壳动态域名解析服务（DDNS）实现外网域名访问。感谢《网络安全法》的出台，花生壳域名需要实名验证才能继续使用，实在懒得上传资料验证，索性直接使用外网IP访问服务器。唯一的问题是路由器重启后，重新拨号获得的外网IP也会变化，需要以某种方式通知项目组成员。因为公司在使用钉钉，所以自然而然地想到了钉钉的群机器人功能。

实现钉钉机器人推送内容很容易，具体请自行查看钉钉自定义机器人文档。外网IP是通过访问IP138提取网页内容得到，相关代码如下：

```python
#!/usr/bin/env python3
# coding=utf-8
import requests
import json


def ding_talk_push(content):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=' \
          '*********替换为自己的地址**************'
    headers = {"Content-Type": "application/json ;charset=utf-8 "}
    string_text_msg = {"msgtype": "text", "text": {"content": content}}
    string_text_msg = json.dumps(string_text_msg)
    requests.post(url, data=string_text_msg, headers=headers)


def get_ext_ip():
    url = r'http://1212.ip138.com/ic.asp'
    r = requests.get(url)
    text = r.text
    ip = text[text.find("[") + 1: text.find("]")]
    return ip


if __name__ == '__main__':

    ExtIP = get_ext_ip()
    fp = open('ExtIP.txt')
    LastExtIP = fp.read()
    fp.close()
    if LastExtIP == ExtIP:
        pass
    else:
        ding_talk_push("外网IP：" + ExtIP)
        fp2 = open('ExtIP.txt', 'w')
        fp2.write(ExtIP)
        fp2.close()
```

程序运行可以自动推送外网IP（如果变了的话）到钉钉群里面。接下来设置程序工作日的早上九点自动执行，Gitlab服务器运行在Ubuntu/Linux下，任务定时执行可以直接通过*crontab*实现，上面的脚本保存为*DingTalkBot.py*，打开终端，执行

```shell
crontab -e
```

编辑*crontab*文件，添加如下内容：

```shell
0 9 * * 1,2,3,4,5 /pathto/python /pathto/DingTalkBot.py
```

**参数说明**

```shell
*     *     *   *    *        command to be executed
-     -     -   -    -
|     |     |   |    |
|     |     |   |    +----- day of week (0 - 6) (Sunday=0)
|     |     |   +------- month (1 - 12)
|     |     +--------- day of        month (1 - 31)
|     +----------- hour (0 - 23)
+------------- min (0 - 59)
```

**注意：**路径都使用绝对路径

---

**Update**

由于IP 138改版，原有获取外网IP函数失效，将其替换为如下即可

```python
from urllib.request import urlopen
def get_ext_ip():
    ip = json.load(urlopen('http://httpbin.org/ip'))['origin']
    return ip
```
