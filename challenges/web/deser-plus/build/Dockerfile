FROM ghcr.io/w4terdr0p/w4terctf-2023/php:alpine-7.4 AS builder

RUN apk add --no-cache libxml2-dev && \
    docker-php-ext-configure soap && \
    docker-php-ext-install soap

FROM builder AS final

COPY --from=builder /usr/local/lib/php/extensions/* /usr/local/lib/php/extensions/

COPY index.php flag.php /var/www/html/
RUN chown -R www-data:www-data /var/www/html/

COPY php.ini /usr/local/etc/php/conf.d/
COPY --chmod=500 init.sh /etc/init.sh

CMD ["/etc/init.sh"]
