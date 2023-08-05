#!/bin/sh

# Keep the GZCTF_FLAG environment variable
# Also export the FLAG environment variable
export FLAG=$GZCTF_FLAG

su newnew -c 'env flask run -h 0.0.0.0 -p 80'
