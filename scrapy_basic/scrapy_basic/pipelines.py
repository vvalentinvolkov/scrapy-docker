import logging

import requests
from scrapy.exceptions import CloseSpider, DropItem

logger = logging.getLogger(__name__)


class HttpPostPipeline:
    """Send dict item by POST request to HTTP_POST_URL with HTTP_POST_HEADERS"""

    def open_spider(self, spider):
        try:
            self.url = spider.settings['HTTP_POST_URL']
            self.headers = spider.settings['HTTP_POST_HEADERS']
        except KeyError:
            logger.error('HTTP_POST_URL and HTTP_POST_HEADERS are required')
            raise CloseSpider

    def process_item(self, item, spider):
        response = requests.post(self.url, json=item, headers=self.headers)
        if response.status_code < 400:
            return item
        elif response.status_code == 400:
            logger.info(f'Response status - {response.status_code}. DropItem')
            raise DropItem
        else:
            logger.error(f'Response status - {response.status_code}. CloseSpider')
            raise CloseSpider

