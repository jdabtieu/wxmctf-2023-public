FROM python:slim

RUN pip3 install gunicorn flask
RUN mkdir /app
ADD . /app

USER nobody
WORKDIR /app
CMD python -m gunicorn wsgi:app --bind 0.0.0.0:8000
