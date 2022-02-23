FROM python:3.6-slim

# set work directory
WORKDIR /usr/src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencie
RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN \
 apt-get -y update && \
 apt-get -y install libpq-dev gcc

RUN pip install -r requirements.txt
