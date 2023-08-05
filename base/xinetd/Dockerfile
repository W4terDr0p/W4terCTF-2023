FROM alpine:latest AS builder

ARG XINETD_VERSION=2.3.15.4

RUN apk add build-base autoconf automake libtool pkgconf git && \
    git clone -b ${XINETD_VERSION} https://github.com/openSUSE/xinetd.git && \
    cd xinetd && sh ./autogen.sh && ./configure && make

FROM alpine:latest

COPY --from=builder /xinetd/xinetd /usr/sbin
RUN mkdir -p /etc/xinetd.d/ && \
    adduser -D -h /home/ctf ctf

CMD ["sleep", "infinity"]
