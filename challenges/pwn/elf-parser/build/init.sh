#!/bin/sh

echo $GZCTF_FLAG > /home/ctf/env/flag
chmod +x /home/ctf/env/elf_parser
chown -R ctf:ctf /home/ctf/env/flag
unset GZCTF_FLAG

timeout 30 /usr/sbin/chroot --userspec=1000:1000 /home/ctf/env /run.sh
