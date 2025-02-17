FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY dogs_project /dogs_project
WORKDIR /dogs_project
EXPOSE 8000

RUN pip install --no-cache-dir -r /temp/requirements.txt  # Добавлено --no-cache-dir для уменьшения размера образа

RUN adduser --disabled-password service-user
USER service-user
