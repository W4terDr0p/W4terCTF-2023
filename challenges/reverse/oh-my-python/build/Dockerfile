FROM python:3.8-alpine

RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple flask && \
    adduser -D -h /home/ctf ctf && \
    mkdir -p /home/ctf/app/static && \
    chown -R ctf:ctf /home/ctf

COPY --chown=ctf:ctf app.py /home/ctf/app
COPY --chown=ctf:ctf --chmod=500 gen.py init.sh /home/ctf/

WORKDIR /home/ctf
USER ctf

CMD ["./init.sh"]
