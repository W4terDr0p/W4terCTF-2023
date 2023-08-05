#!/bin/sh

python gen_code.py "$GZCTF_FLAG"
mv qrcode.png /home/ctf/www/
unset GZCTF_FLAG

cd www && python -m http.server 80
