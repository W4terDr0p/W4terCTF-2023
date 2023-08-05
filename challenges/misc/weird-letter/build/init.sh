#!/bin/sh

cd /opt/weird-letter/ && python gen_html.py "$GZCTF_FLAG"
mv /opt/weird-letter/index.html /var/www/html/index.html
unset GZCTF_FLAG

chmod 644 /var/www/html/index.html
chown -R www-data:www-data /var/www/html/

cd /var/www/html && su www-data -c "python -m http.server 80"
