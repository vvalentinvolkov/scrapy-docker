FROM python:3.10-bullseye

WORKDIR /code/scrapy_basic

COPY ./pyproject.toml /code
COPY ./poetry.lock /code

RUN pip install --no-cache-dir --upgrade poetry ; \
    poetry config virtualenvs.create false ; \
    poetry install

COPY ./scrapy_basic .

VOLUME ./scrapy_basic/spiders

CMD echo "hello"