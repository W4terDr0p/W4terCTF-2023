# Login

**Author:** peigong

**Difficulty:** Medium

**Category:** Crypto

## 题目描述

登录一个系统需要用户对应的证书，而这个服务器把加密后的管理员的证书泄露了出来，要怎么才能得到正确的管理员的证书呢？

## 题目解析

**暴露端口：** 10003

纯纯的 AES padding oracle，只是把它包装了一下而已。 参考 https://robertheaton.com/2013/07/29/padding-oracle-attack/

攻击原理是：攻击是从块的最后一位开始。如下图，我们的目的是构造一个`C1'`，然后使得`P2'`的末尾依次是`\x01`，`\x02\x02`,...,`\x0f\x0f...\x0f`。根据 oracle 的返回，当 padding 没有错误的时候就表示成功构造了这样的一个`P2'`，这样一来由于`C1'`和`P2'`就是已知的，从而通过异或可以把`I2`恢复出来，然后根据已知的`C1`则有`P2 = C1 xor I2`，就可以把`P2`恢复出来了。

![aes_padding_oracle](https://robertheaton.com/images/cbcreal.png)
