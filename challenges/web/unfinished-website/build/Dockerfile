FROM eclipse/alpine_jdk8

USER root
COPY --chmod=500 --chown=user:users init.sh /init.sh
ADD --chmod=555 https://nas.gzti.me/Misc/Assets/unfinished-website.jar /opt/app/unfinished-website.jar
RUN echo "flag{placeholder}" > /flag && chown -R user:users /flag

WORKDIR /opt/app
USER user

CMD ["/init.sh"]
