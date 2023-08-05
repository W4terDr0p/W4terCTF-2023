#!/bin/sh

echo $GZCTF_FLAG > /flag
unset GZCTF_FLAG

java -jar /opt/app/unfinished-website.jar
