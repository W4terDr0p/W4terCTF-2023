FROM node:18-alpine

RUN apk add --no-cache chromium

ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true \
    PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser

USER node
WORKDIR /app
COPY --chown=node:node src .
RUN npm install --registry https://registry.npmmirror.com/

CMD ["node", "app.js"]
