# Maze Digger

**Author:** GZTime

**Difficulty:** Hard

**Category:** Reverse

## 题目描述

在获取 GZTime 的魔法书的过程中，你的意识不小心进入了他创建的诡异迷宫！

在这个危急时刻，你只有通过提交这个迷宫的解法才能醒来！

似乎这个迷宫是用一种叫做 WebAssembly 的异世界魔法创建的，而且据说这个迷宫中还会有一些神秘的 Rust 出没！

英勇如你，一定能重新夺回自己的意识！

Note：可以使用 `wasmtime` 运行 wasm 文件。

## 题目解析

**暴露端口：`70`**

逆向 wasm，获取迷宫及其解密方式，之后通过搜索算法得到迷宫的路径并提交。
