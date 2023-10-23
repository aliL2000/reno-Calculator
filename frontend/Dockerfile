FROM node:latest

WORKDIR /src

COPY frontend/package.json .
COPY frontend/package-lock.json .

RUN npm ci

COPY frontend/ .

EXPOSE 3000

CMD ["npm", "run", "dev"]