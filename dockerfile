FROM python:3.10-bullseye

WORKDIR /home/scrapy_basic

RUN pip install scrapy

COPY ./scrapy_basic .

VOLUME ./scrapy_basic/spiders

CMD echo "hello"