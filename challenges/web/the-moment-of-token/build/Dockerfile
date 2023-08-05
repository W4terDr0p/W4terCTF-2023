FROM python:alpine

RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple flask jwcrypto && \
    adduser -D -h /home/ctf ctf && \
    mkdir -p /home/ctf/app

COPY src /home/ctf/app

WORKDIR /home/ctf/app
USER ctf

CMD ["python", "app.py"]
