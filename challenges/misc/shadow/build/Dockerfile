FROM python:alpine

RUN adduser -D -h /home/ctf ctf

COPY --chown=ctf:ctf chall.py /home/ctf/
COPY --chmod=500 init.sh /init.sh

CMD ["/init.sh"]
