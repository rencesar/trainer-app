# pull official base image
FROM python:3.8-alpine

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /app

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

# install dependencies
COPY ./Pipfile /app/Pipfile

RUN pip install --upgrade pip \
    && pip install pipenv \
    && pipenv install --skip-lock --system --dev

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/entrypoint.sh

# Give entrypoint permitions
RUN chmod +x /usr/src/entrypoint.sh
