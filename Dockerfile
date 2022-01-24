FROM python:3.8.12-alpine

WORKDIR /app

COPY ./requirements.txt .

RUN apk update\
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-connector-c-dev\
    && pip install -r requirements.txt \
    && apk del build-deps

COPY . .

CMD['gunicorn']