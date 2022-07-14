FROM nginx:latest
MAINTAINER Dobob dobob@dobob.kr

COPY . /usr/share/nginx/html

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/
RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d	
