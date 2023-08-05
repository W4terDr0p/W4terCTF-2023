#!/bin/sh

echo $GZCTF_FLAG > /home/ctf/esp/FLAG
unset GZCTF_FLAG

chown -R ctf:ctf /home/ctf
killall -9 qemu-system-x86_64 2>/dev/null || true
rm -rf /home/ctf/esp/APP/EXE

python /home/ctf/run.py
