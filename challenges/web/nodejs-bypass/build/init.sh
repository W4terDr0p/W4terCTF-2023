#!/bin/sh

export SECRET_COOKIE=$(echo $RANDOM | md5sum |cut -c 1-8)

echo $GZCTF_FLAG | cut -c 1-20 > /flag1
echo $GZCTF_FLAG | cut -c 21- > /flag2
unset GZCTF_FLAG

rm -f ./start.sh

cd /www/app && su www-data -c "node main.js"
