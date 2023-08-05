# Middleman

**Author:** peigong

**Difficulty:** Trivial

**Category:** Crypto

## 题目描述

GZTime 在和某人偷偷交流 flag， 但他们也太大意了，竟然不认证对方的身份，你能偷偷把 flag 拿过来吗。

## 题目解析

**暴露端口：** 10007

DH 密钥协商的中间人攻击，自己生成一个私钥发给通信双方，然后就可以进行通信并拿到 flag 了
