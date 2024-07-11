FROM python:3.10-alpine

WORKDIR /code

#RUN apt-get update
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt
