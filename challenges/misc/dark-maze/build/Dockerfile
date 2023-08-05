FROM ghcr.io/w4terdr0p/w4terctf-2023/numpy:latest

RUN apt update && apt install -y --no-install-recommends xinetd && rm -rf /var/lib/apt/lists/*
COPY --chmod=500 init.sh main.py /
COPY xinetd.conf /etc/xinetd.conf

CMD ["xinetd", "-dontfork"]
