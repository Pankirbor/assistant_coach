FROM python:3.11-slim

RUN apt-get clean && apt-get update && apt-get install -qy nano

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./ ./
