FROM ghcr.io/w4terdr0p/w4terctf-2023/python:alpine

COPY --chown=ctf:ctf chall.py maze.txt /home/ctf/
COPY xinetd.conf /etc/xinetd.conf
COPY --chmod=500 init.sh /init.sh

WORKDIR /home/ctf

CMD ["/init.sh"]
