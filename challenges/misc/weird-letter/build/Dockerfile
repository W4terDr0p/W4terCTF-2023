FROM python:alpine

COPY --chmod=755 init.sh /

RUN mkdir -p /opt/weird-letter/ \
    && mkdir -p /var/www/html/ \
    && adduser -D -G www-data -s /bin/ash -h /var/www/html/ www-data

COPY gen_html.py template.html /opt/weird-letter/
COPY robots.txt n0_h1nt_her3.html /var/www/html/

CMD ["/init.sh"]
