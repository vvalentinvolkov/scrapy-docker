**Docker container for launching scrapy spiders.**
---
# Dockerfile #

    FROM python:3.10-bullseye

    WORKDIR /home/scrapy_basic
    
    RUN pip install scrapy
    
    COPY ./scrapy_basic .
    
    VOLUME ./scrapy_basic/spiders
    
    CMD echo "hello"

# Settings #

    CLOSESPIDER_TIMEOUT = 300 
    CLOSESPIDER_ITEMCOUNT
    CLOSESPIDER_PAGECOUN
    CLOSESPIDER_ERRORCOUNT
    LOG_LEVEL = 'INFO'
    HTTP_POST_URL

# Usage #

**Spider** - The mounted directory must contain SPIDER_NAME.py with scrapy spider which name is the same.

**Output** - There will be output file.

**Logs** - If there is SPIDER_NAME.log file logs will redirect to it. 