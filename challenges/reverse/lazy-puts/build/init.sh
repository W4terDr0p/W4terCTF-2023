#!/bin/sh

python gen.py

unset GZCTF_FLAG

cd app && python app.py
