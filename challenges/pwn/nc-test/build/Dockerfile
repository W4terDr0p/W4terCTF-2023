FROM ghcr.io/w4terdr0p/w4terctf-2023/xinetd:alpine

COPY --chmod=755 getflag /getflag
COPY xinetd.conf /etc/xinetd.conf

CMD ["xinetd", "-dontfork"]
