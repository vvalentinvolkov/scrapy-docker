FROM python:3.9.9-bullseye

WORKDIR /home/scrapy_basic

RUN pip install scrapy

COPY ./scrapy_basic .
VOLUME ./scrapy_basic/spiders

CMD scrapy crawl $SPIDER_NAME