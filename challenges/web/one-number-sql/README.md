# One Number SQL

**Author:** tel

**Difficulty:** Normal

**Category:** Web

## 题目描述

GZTime 把 flag 藏到数据库里，只给大家看 flag 的一小截，但是这不影响你拿到 flag 吧 ~

## 题目解析

**暴露端口：`80`**

注入点在 `len`，waf 过滤了数字，要求数字不能大于 10，小于 1

此处可以进行拼接绕过，然而，正常情况下，查到的 flag 在 `result[1]`，环境中只会输出 `result[0]`。

所以需要将 sql 只输出一行，拼接 `where 'a'='b'` 将 `result[0]` 屏蔽掉，这样 `result[1]` 就顺到 `result[0]` 了

`-1) from flag where 'a'='b' union select flag from flag-- qwe`

或者，在 `substr` 里面插入 `hex('a')+1` 也是可以的
