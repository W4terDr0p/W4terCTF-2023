FROM node:lts-alpine3.15

COPY app /www/app
COPY --chmod=500 init.sh /init.sh

WORKDIR /www/app
RUN adduser -D -G www-data -s /bin/ash www-data && \
    npm --registry https://registry.npmmirror.com/ install

CMD ["/init.sh"]
