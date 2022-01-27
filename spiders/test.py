import os

from scrapy import Spider, Request


class SpiderTest(Spider):
    name = "test"

    def start_requests(self):
        urls = [
            'https://www.google.com/',
        ]
        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        return dict(response.headers)
