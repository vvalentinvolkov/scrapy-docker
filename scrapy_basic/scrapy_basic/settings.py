import os

SPIDER_NAME = os.environ.get('SPIDER_NAME')
log_file_path = f'scrapy_basic/spiders/{SPIDER_NAME}.log'

LOG_LEVEL = 'INFO'
LOG_FILE = log_file_path if os.path.exists(log_file_path) else None

# FEED_FORMAT = 'csv'
# FEED_URI = f'scrapy_basic/spiders/{SPIDER_NAME}.csv'
# FEED_EXPORT_FIELDS = []

SPIDER_MODULES = ['scrapy_basic.spiders']
NEWSPIDER_MODULE = 'scrapy_basic.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36.'

COOKIES_ENABLED = False
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 2

CLOSESPIDER_TIMEOUT = 300   # Ограничение по времени в секундах
# CLOSESPIDER_ITEMCOUNT = 10   # Ограничение по колличеству item вовзращенных из функций *_parse
# CLOSESPIDER_PAGECOUN = 50  # Ограничение по колличеству страниц
# CLOSESPIDER_ERRORCOUNT = 5   # Ограничение по колличеству поднятых встроенных ошибок scrapy_project

SPIDER_MIDDLEWARES = {
   'scrapy.spidermiddlewares.offsite.OffsiteMiddleware': 100,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 300,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

EXTENSIONS = {
    'scrapy.extensions.closespider.CloseSpider': 100,
}

ITEM_PIPELINES = {
   'scrapy_basic.pipelines.HttpPostPipeline': 300,
}
