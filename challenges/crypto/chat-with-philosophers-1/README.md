# Chat with Philosophers 1

**Author:** peigong

**Difficulty:** Easy

**Category:** Crypto

## 题目描述

小明 最近学习 CTF 比较的空虚，因此他请教了哲学家尼采，希望他的超人理论能帮他从空虚中解救出来。

但尼采要求小明先用椭圆曲线和他进行密钥交换才能开始聊天。。。。

## 题目解析

**暴露端口：** `10004`

密钥协商用到的曲线都是弱曲线，用 pohlig-hellman 算法就可以求出两个私钥，然后得到协商的密钥，然后通过 AES 解密即可。
