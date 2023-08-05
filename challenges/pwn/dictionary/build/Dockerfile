FROM ubuntu:20.04 AS builder

COPY src/dictionary.c /dictionary.c
RUN apt update && \
    apt --no-install-recommends install -y gcc gcc-multilib && \
    gcc -o /dictionary /dictionary.c

FROM ghcr.io/w4terdr0p/w4terctf-2023/xinetd:alpine

COPY init.sh /init.sh
COPY xinetd.conf /etc/xinetd.conf

RUN chmod +x /init.sh && \
    chown -R ctf:ctf /home/ctf && \
    chmod -R 750 /home/ctf && \
    cp -R /lib* /home/ctf && \
    mkdir /home/ctf/lib64  && \
    mkdir /home/ctf/dev  && \
    mknod /home/ctf/dev/null c 1 3 && \
    mknod /home/ctf/dev/zero c 1 5 && \
    mknod /home/ctf/dev/random c 1 8 && \
    mknod /home/ctf/dev/urandom c 1 9 && \
    chmod 666 /home/ctf/dev/* && \
    mkdir /home/ctf/bin && \
    mkdir -p /home/ctf/lib/x86_64-linux-gnu/ && \
    cp /bin/sh /home/ctf/bin && \
    cp /bin/ls /home/ctf/bin && \
    cp /bin/cat /home/ctf/bin && \
    cp /bin/base64 /home/ctf/bin

COPY --from=builder /lib/x86_64-linux-gnu/ld-linux-x86-64.so.2 /home/ctf/lib64/
COPY --from=builder /lib/x86_64-linux-gnu/libc.so.6 /home/ctf/lib/x86_64-linux-gnu/
COPY --from=builder --chown=ctf:ctf --chmod=500 /dictionary /home/ctf/

CMD ["xinetd", "-dontfork"]
