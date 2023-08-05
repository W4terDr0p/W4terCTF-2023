# php 基础镜像

## 使用方式

启动 nginx 和 php，`init.sh` 使用示例：

```bash
#!/bin/sh
echo $GZCTF_FLAG > /flag
chmod 444 /flag
unset GZCTF_FLAG

php-fpm -D
nginx -g 'daemon off;'
```
