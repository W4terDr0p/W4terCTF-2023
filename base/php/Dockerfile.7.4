FROM php:7.4.0-fpm-alpine

RUN apk add --no-cache shadow nginx && mkdir -p /run/nginx && \
    usermod -u 1000 www-data && \
    groupmod -g 1000 www-data && \
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

COPY php.ini /usr/local/etc/php/conf.d/php.ini
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --chown=www-data:www-data index.php /var/www/html
COPY --chmod=500 init.sh /init.sh

CMD ["/init.sh"]
