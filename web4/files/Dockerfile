FROM node:19-slim
EXPOSE 8080
RUN apt-get update && apt-get install sqlite3 -y
WORKDIR /shop
COPY . /shop
RUN npm install
RUN sqlite3 data.db < schema.sql
CMD node setup.js && node .
