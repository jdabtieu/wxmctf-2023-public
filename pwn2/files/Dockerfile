FROM openjdk:11-slim

EXPOSE 5000

RUN apt update && apt install -y socat
RUN mkdir /app
COPY ExprChecker.class /app/ExprChecker.class
COPY flag.txt /flag.txt

WORKDIR /app
RUN chmod 777 /app
USER nobody
ENTRYPOINT socat tcp-l:5000,reuseaddr,fork EXEC:"java ExprChecker",pty,stderr,echo=0
