# NC Test

**Author:** GZTime

**Difficulty:** Baby

**Category:** Pwn

## 题目描述

迈向 CTF 的第一步！

在 CTF 中使用 netcat (nc) 建立连接是相当经常且重要的。你能连接到服务器，以获得这题的 Flag 吗？

nc 的全名是 netcat，其主要用途是建立和监听任意 TCP 和 UDP 连接，支持 IPv4 和 IPv6，可以用来网络调试、端口扫描等等。

这是一篇介绍 nc 的文章：[netcat 的使用](https://www.cnblogs.com/Lmg66/p/13811636.html)

假设给出的实例入口为 `host:port`，那么你可以使用 `nc host port` 来连接到对应的实例。

## 题目解析

**暴露端口：`70`**

直接 nc 连接到服务器即可获取 flag。
