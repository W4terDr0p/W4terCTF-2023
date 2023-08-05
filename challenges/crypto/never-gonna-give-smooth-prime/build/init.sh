#!/bin/sh

echo "flag = b\"$GZCTF_FLAG\"" > /home/ctf/secret.py
unset GZCTF_FLAG

chown -R ctf:ctf /home/ctf/

xinetd -dontfork
