#!/bin/sh

echo "$GZCTF_FLAG" > /home/ctf/flag.txt
unset GZCTF_FLAG

chown -R ctf:ctf /home/ctf/

xinetd -dontfork
