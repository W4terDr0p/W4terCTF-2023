#!/bin/sh

cd /opt/bad-code/ && python gen_code.py "$GZCTF_FLAG"
mv /opt/bad-code/qrcode.png /home/ctf/www/
unset GZCTF_FLAG

chmod 644 /home/ctf/www/qrcode.png
chown -R ctf:ctf /home/ctf/www/

cd /home/ctf/www/ && su ctf -c "python -m http.server 80"
