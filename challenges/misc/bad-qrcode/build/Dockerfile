FROM ghcr.io/w4terdr0p/w4terctf-2023/numpy

RUN pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple/ qrcode pillow && \
    useradd -rm -s /bin/bash ctf && \
    mkdir -p /opt/bad-code/ && mkdir -p /home/ctf/www/

COPY gen_code.py /opt/bad-code/
COPY --chmod=644 --chown=ctf:ctf index.html /home/ctf/www/
COPY --chmod=500 init.sh /

CMD ["/init.sh"]
