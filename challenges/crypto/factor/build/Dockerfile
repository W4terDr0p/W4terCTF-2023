FROM ghcr.io/w4terdr0p/w4terctf-2023/gmpy2:alpine

COPY --chown=ctf:ctf chall.py /home/ctf
COPY --chmod=500 init.sh /init.sh

CMD ["/init.sh"]
