FROM ghcr.io/w4terdr0p/w4terctf-2023/python:alpine

COPY --chmod=555 init.sh main.py /
COPY xinetd.conf /etc/xinetd.conf

CMD ["xinetd", "-dontfork"]
