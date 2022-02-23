#############################################
# BUILDER IMAGE: Only for building the code #
#############################################
# FROM python:3.8-slim-buster AS builder
# Soon...

######################################
# RUNNER IMAGE: For running the code #
######################################
FROM python:3.6-slim

# Set work directory
WORKDIR /usr/src

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install here only runtime required packages
RUN \
 apt-get -y update && \
 apt-get -y install libpq-dev gcc

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy the project files
COPY apps/ apps/
COPY djangoAPI/ djangoAPI/
COPY manage.py .
COPY scripts/ scripts/
