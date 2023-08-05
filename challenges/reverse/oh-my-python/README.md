# Oh My Python

**Author:** GZTime

**Difficulty:** Trivial

**Category:** Reverse

## 题目描述

据说 GZTime 把 flag 藏在了一份 python 脚本中，但是他已经把原文件删除了！

我们只在他的 `__pycache__` 文件夹中找到了一份 `pyc` 文件，你找到 flag 吗？

Note: 新建实例时会实时生成附件，浏览器访问即可下载，多次新建实例会导致附件不同，但是不影响 flag 内容。

## 题目解析

**暴露端口：`80`**

uncompyle6 直接上，之后写脚本稍微爆破一下数字组合，异或后就能得到 flag 了。
