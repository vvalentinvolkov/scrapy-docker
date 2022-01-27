**Docker container for launching scrapy spiders.**
---
# Dockerfile #

    FROM python:3.9.9-bullseye

    WORKDIR /home/scrapy_basic

    RUN pip install scrapy

    COPY ./scrapy_basic .

    VOLUME ./scrapy_basic/spiders

    CMD scrapy crawl $SPIDER_NAME

# Default settings #
    CLOSESPIDER_TIMEOUT = 300 
    LOG_LEVEL = 'INFO'

# Usage #

**Spider** - The mounted directory must contain SPIDER_NAME.py with scrapy spider which's name is the same.

**Output** - There will be output file.

**Logs** - If there is SPIDER_NAME.log file logs will redirect to it. 