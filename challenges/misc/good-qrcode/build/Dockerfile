FROM python:alpine

RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple qrcode pillow && \
    adduser -D -h /home/ctf ctf && \
    mkdir -p /home/ctf/www/ && \
    chown -R ctf:ctf /home/ctf

COPY gen_code.py /home/ctf/
COPY --chmod=644 --chown=ctf:ctf index.html /home/ctf/www/
COPY --chmod=500 --chown=ctf:ctf init.sh /

WORKDIR /home/ctf/
USER ctf

CMD ["/init.sh"]
