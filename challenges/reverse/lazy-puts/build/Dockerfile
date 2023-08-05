FROM python:alpine

RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple flask && \
    adduser -D -h /home/ctf ctf && \
    mkdir -p /home/ctf/app/ && \
    chown -R ctf:ctf /home/ctf

COPY --chown=ctf:ctf app.py /home/ctf/app

# compile origin from source.c in github action
# gcc source.c -o origin -fno-stack-protector -no-pie -O2
COPY --chown=ctf:ctf --chmod=500 origin gen.py init.sh /home/ctf/

WORKDIR /home/ctf
USER ctf

CMD ["./init.sh"]
