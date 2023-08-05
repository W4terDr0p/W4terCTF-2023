FROM ubuntu:22.04 AS builder

COPY ./diff.patch /diff.patch
RUN apt update && \
    apt --no-install-recommends install -y cmake gcc python3 apt-transport-https ca-certificates git make gcc-multilib && \
    update-ca-certificates

RUN git clone https://github.com/jerryscript-project/jerryscript.git && \
    cd jerryscript && \
    git checkout 6fe763f1912c3ef82ec2ca31c40f186dde9c5a57 && \
    git apply ../diff.patch && \
    mkdir build && \
    cd build && \
    python3 ../tools/build.py --debug --compile-flag="-Wl,-z,norelro" && \
    cd ../

FROM ubuntu:22.04

COPY init.sh /init.sh

RUN apt update && \
    apt --no-install-recommends -y install xinetd && useradd -m ctf && groupadd -f ctf && \
    chmod +x /init.sh && \
    mkdir -p /home/ctf/lib/ && \
    cp -R /usr/lib/x86_64-linux-gnu /home/ctf/lib/ && \
    cp -R /usr/lib32 /home/ctf && \
    cp -R /usr/lib64 /home/ctf && \
    mkdir /home/ctf/dev  && \
    mknod /home/ctf/dev/null c 1 3 && \
    mknod /home/ctf/dev/zero c 1 5 && \
    mknod /home/ctf/dev/random c 1 8 && \
    mknod /home/ctf/dev/urandom c 1 9 && \
    chmod 666 /home/ctf/dev/* && \
    mkdir /home/ctf/bin && \
    chown -R ctf:ctf /home/ctf && \
    chmod -R 750 /home/ctf && \
    cp /bin/sh /bin/ls /bin/cat /bin/base64 /bin/timeout /bin/bash /home/ctf/bin/ && \
    mkdir -p /home/ctf/usr/libexec/coreutils/ && \
    cp /usr/libexec/coreutils/libstdbuf.so /home/ctf/usr/libexec/coreutils/libstdbuf.so

COPY xinetd.conf /etc/xinetd.conf
COPY --chmod=500 --chown=ctf:ctf run.sh /home/ctf/run.sh
COPY --from=builder --chown=ctf:ctf /jerryscript/build/bin/jerry /home/ctf/jerry

CMD ["xinetd", "-dontfork"]
