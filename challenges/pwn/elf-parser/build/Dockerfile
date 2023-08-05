FROM ubuntu:22.04

COPY init.sh /init.sh

RUN apt update && apt --no-install-recommends -y install xinetd && \
    useradd -m ctf && groupadd -f ctf && \
    chmod +x /init.sh && mkdir -p /home/ctf/env/ && \
    cp -R /usr/lib* /home/ctf/env && \
    mkdir /home/ctf/env/dev  && \
    mknod /home/ctf/env/dev/null c 1 3 && \
    mknod /home/ctf/env/dev/zero c 1 5 && \
    mknod /home/ctf/env/dev/random c 1 8 && \
    mknod /home/ctf/env/dev/urandom c 1 9 && \
    chmod 666 /home/ctf/env/dev/* && \
    mkdir /home/ctf/env/bin && \
    chmod -R 750 /home/ctf/env && \
    chown -R ctf:ctf /home/ctf/env && \
    cp /bin/sh /bin/ls /bin/cat /bin/base64 /bin/timeout /home/ctf/env/bin

COPY xinetd.conf /etc/xinetd.conf
COPY --chmod=500 --chown=ctf:ctf run.sh elf_parser /home/ctf/env/

CMD ["xinetd", "-dontfork"]
