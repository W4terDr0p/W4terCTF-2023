# Never Gonna Give Smooth Prime

**Author:** ZMJ

**Difficulty:** Medium

**Category:** Crypto

## 题目描述

Never gonna give smooth prime

Never gonna get the flag

## 题目解析

**暴露端口：`1337`**

首先 `pad` 是确定的结果，所以说 `pad` 之后是一个确定的 256bytes，也就是确定的 2048 位数 $x$。

然后有 $g^x \equiv y \pmod{p}$

然后是强素数 $p$ 的定义：在数论中，$p$ 为强素数，当 $p-1$ 和 $p+1$ 具有大的素因子。此时上面的离散对数一般认为是不可解的（不可实际地被解出）。更细节的可以看下面的文档：

<https://pycryptodome.readthedocs.io/en/latest/src/util/util.html?highlight=getStrongPrime#Crypto.Util.number.getStrongPrime>

但是同时注意，强素数仅意味着 $p-1$ 具有大的素因子，**可能此时也同时具有比较小的素因子**，譬如 $p-1 = 2 q_0 q_1$，其中 $q_0$ 较小，$q_1$ 较大这种的，那么我们就可以利用求离散对数的方法求出 $x \bmod q_0$ 的值。

然后因为我们的 flag 内容不变，$x$ 值也是不变的， 我们可以多次询问服务器，得到若干组 $x \bmod q_0$ 的值。当我们的值足够多的时候，就可以利用中国剩余定理求得 $x$ 的值。
