FROM ghcr.io/w4terdr0p/w4terctf-2023/python:alpine

RUN mkdir -p /app && \
    pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple flask random-password-generator && \
    adduser -D -G www-data -s /bin/ash -h /app www-data

COPY --chmod=500 --chown=www-data:www-data app.py init.py /app/
COPY templates/ /app/templates/
COPY --chmod=500 --chown=www-data:www-data init.sh /etc/init.sh

WORKDIR /app
USER www-data

CMD ["/etc/init.sh"]
