FROM python:3.10-alpine3.15

WORKDIR /app
RUN apk add gcc
RUN apk add python3-dev

COPY requirements.txt app/requirements.txt
RUN pip install -r app/requirements.txt

COPY . /app

