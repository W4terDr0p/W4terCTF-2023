# Special RSA

**Author:** peigong

**Difficulty:** Medium

**Category:** Crypto

## 题目描述

So much has been leaked, can't be done?

OhHHHH! Common prime RSA can make it.

## 题目解析

**暴露端口：** 10001

已知 g 的 common prime RSA， 上网随便搜搜就能搜到解法，这里把解题过程写一下。

common prime RSA 满足：

$$p=2ag+1\\ q = 2bg+1$$

其中 $a,b,g$ 为素数。

从$g$的取值可见 $g<a+b$。因此有方程 $\frac{N-1}{2g} = 2gv+u$，从而计算出 $u$ 和 $0\leq v\leq 2g$。

由方程 $N-1=2g(2gab+a+b)$ 可得

$$a+b-2gc=v \\ ab+c=u$$

其中 $c$ 为未知数。

随机选取一个与 $N$ 互素的整数 $x$，则有 $$x^{2gu}\equiv x^{2g(ab+c)}\mod N$$ 又根据模 $N=pq$ 下乘法群的性质，$x$ 的阶为卡迈克尔函数取 $N$ 时的值，即 $x^{2gab}\equiv 1\mod N$。因此有 $x^{2gu}\equiv x^{2gc}\mod N$，令 $y=x^{2g}\mod N$，则有 $y^u\equiv y^c\mod N$。 现在就变成求解模 $N$ 下的离散对数问题，由于 $g$ 的选取，因此 $c$ 比较小，用大步小步法就能在 20s 内把 $c$ 求解出来。然后根据上面的方程可以求解出 $a,b$，从而计算出 $p,q$。
