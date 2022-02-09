import os

from scrapy import Spider, Request


class SpiderTest(Spider):
    name = "test"

    custom_settings = {
        'HTTP_POST_URL': os.environ["HTTP_POST_URL"],
        'HTTP_POST_HEADERS': {
            'Authorization': f'Token {os.environ["HTTP_POST_AUTH_TOKEN"]}',
            'Content-type': 'application/json'
        }
    }

    def start_requests(self):
        urls = [
            'https://www.google.com/',
        ]
        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        return dict(response.headers)
