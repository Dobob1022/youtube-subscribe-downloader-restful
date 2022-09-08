FROM python:3.10.5
MAINTAINER Dobob dobob@dobob.kr

RUN mkdir /app
COPY requirements.txt /
RUN pip3 install -U pip
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app


