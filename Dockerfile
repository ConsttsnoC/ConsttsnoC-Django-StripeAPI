# syntax=docker/dockerfile:1
FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /web_django
WORKDIR /web_django
COPY requirements.txt /web_django/
RUN pip install --upgrade pip && pip install -r requirements.txt && echo ls
ADD ../.. /web_django/
EXPOSE 8000