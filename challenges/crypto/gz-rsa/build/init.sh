#!/bin/sh

echo $GZCTF_FLAG > flag
export GZCTF_FLAG=""

python chall.py
