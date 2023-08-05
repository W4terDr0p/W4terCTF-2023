FROM ghcr.io/w4terdr0p/w4terctf-2023/python:alpine

COPY xinetd.conf /etc/xinetd.conf
COPY --chmod=500 chall.py init.sh /

CMD ["/init.sh"]
