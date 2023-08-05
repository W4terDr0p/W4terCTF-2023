# GZ_RSA

**Author:** peigong

**Difficulty:** Trivial

**Category:** Crypto

## 题目描述

在 RSA 中，素数的选择和保密性非常重要。

只要不泄露 n 的分解，那 RSA 就是安全的。

## 题目解析

**暴露端口：** `10008`

只有 2000 个素数，多获取几次数据，然后可以用 gcd 就可以把某些 n 分解了，然后得到 flag。手动控制了一下，大概在获取 20 个左右 n 就能找到一些有共同因子的 n。
