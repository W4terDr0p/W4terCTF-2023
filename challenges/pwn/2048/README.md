# 2048

**Author:** Xia0o0o0o

**Difficulty:** Normal

**Category:** Pwn

## 题目描述

Make despair into your stepladders for the sake of flag!

Play 2048 game in your terminal! Get 8192 to win!

## 题目解析

**暴露端口：`70`**

有三种可能可行的方法：

- 玩到 8192
- 利用 `scanf()` 的栈溢出 （不行）
- 字符串格式化

Source code of the game: https://rosettacode.org/wiki/2048
