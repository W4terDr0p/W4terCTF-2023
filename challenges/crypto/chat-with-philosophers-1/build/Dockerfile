FROM ghcr.io/w4terdr0p/w4terctf-2023/gmpy2:alpine

RUN pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple/ sympy

COPY --chown=ctf:ctf chall.py ec.py secret.py /home/ctf/
COPY --chmod=500 --chown=ctf:ctf init.sh /init.sh

USER ctf
WORKDIR /home/ctf

CMD ["/init.sh"]
