FROM node:22-slim

WORKDIR /web

COPY ../../web/package*.json ./
RUN npm install

COPY ../../web/. .

## EXPOSE [Port you mentioned in the vite.config file]

EXPOSE 5173


