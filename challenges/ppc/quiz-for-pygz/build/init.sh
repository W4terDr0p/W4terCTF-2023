#!/bin/sh

echo "$GZCTF_FLAG" > /flag.txt
unset GZCTF_FLAG

xinetd -dontfork
