FROM python:3.8-alpine

LABEL Organization="Xp0int" Author="Rieß"

ENV FLASK_APP=app FLASK_ENV=production FLASK_DEBUG=True

RUN mkdir -p /app; \
    pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple flask && \
    addgroup newnew && \
    adduser -D -G newnew -s /bin/ash -h /app newnew && \
    chown -R newnew:newnew /app && \
    echo -e "new new: flag{dummy_flag}~~\nnew new:where is the real flag?" > /flag && \
    chown newnew:newnew /flag

COPY --chmod=500 init.sh /init.sh
COPY src app/

WORKDIR /app

CMD ["/init.sh"]
