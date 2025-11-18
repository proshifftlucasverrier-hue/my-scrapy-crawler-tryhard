# Scrapy settings for my_scrapy_crawler project

BOT_NAME = 'my_scrapy_crawler'

SPIDER_MODULES = ['my_scrapy_crawler.spiders']
NEWSPIDER_MODULE = 'my_scrapy_crawler.spiders'

# User-Agent string to identify the crawler
USER_AGENT = 'my_scrapy_crawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Enable or disable spider middlewares
# SPIDER_MIDDLEWARES = {
#     'my_scrapy_crawler.middlewares.MyScrapyCrawlerSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# DOWNLOADER_MIDDLEWARES = {
#     'my_scrapy_crawler.middlewares.MyScrapyCrawlerDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# EXTENSIONS = {
#     'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# ITEM_PIPELINES = {
#     'my_scrapy_crawler.pipelines.MyScrapyCrawlerPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# AUTOTHROTTLE_ENABLED = True
# AUTOTHROTTLE_START_DELAY = 5
# AUTOTHROTTLE_MAX_DELAY = 60
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# The AutoThrottle extension will adjust the download delay based on the load of the website being crawled.

# Enable and configure HTTP caching (disabled by default)
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'