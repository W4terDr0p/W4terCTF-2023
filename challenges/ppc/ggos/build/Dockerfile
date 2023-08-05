FROM ghcr.io/w4terdr0p/w4terctf-2023/python:alpine

RUN apk add --no-cache qemu-system-x86_64 xz

COPY --chown=ctf:ctf esp /home/ctf/esp
COPY --chown=ctf:ctf OVMF.fd run.py /home/ctf/
COPY --chmod=500 init.sh /init.sh
COPY xinetd.conf /etc/xinetd.conf

CMD ["xinetd", "-dontfork"]
