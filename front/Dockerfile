FROM node:20.11-bookworm
WORKDIR /app

COPY ./package.json ./
COPY ./yarn.lock ./
RUN yarn

ENTRYPOINT ["yarn", "dev", "--host", "0.0.0.0"]
