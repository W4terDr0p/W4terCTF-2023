#!/bin/bash

echo $GZCTF_FLAG > /home/ctf/flag
chown -R ctf:ctf /home/ctf/flag
export GZCTF_FLAG=""

stdbuf -i0 -o0 -e0 /usr/sbin/chroot --userspec=1000:1000 /home/ctf /run.sh
