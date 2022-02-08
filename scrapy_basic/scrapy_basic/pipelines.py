import logging

import requests
from scrapy.exceptions import CloseSpider, DropItem

logger = logging.getLogger(__name__)


class HttpPostPipeline:
    """Send dict item by POST request to HTTP_POST_URL with HTTP_POST_HEADERS"""
    url: str
    headers: dict

    def open_spider(self, spider):
        try:
            self.url = spider.settings['HTTP_POST_URL']
            self.headers = spider.settings['HTTP_POST_HEADERS']
        except KeyError:
            logger.error('HTTP_POST_URL and HTTP_POST_HEADERS are required')
            raise CloseSpider

    def process_item(self, item, spider):
        response = requests.post(self.url, data=item, headers=self.headers)
        logger.debug(response)
        # TODO: Close spider when bad status code
        if 200 <= response.status_code < 300:
            return item
        else:
            logger.info(f'Response status - {response.status_code}. DropItem')
            raise DropItem

