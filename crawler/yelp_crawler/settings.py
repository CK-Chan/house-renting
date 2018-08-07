# -*- coding: utf-8 -*-
BOT_NAME = 'yelp_crawler'

COMMANDS_MODULE = 'yelp_crawler.commands'
SPIDER_MODULES = ['yelp_crawler.spiders']
NEWSPIDER_MODULE = 'yelp_crawler.spiders'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 ' \
             'Safari/605.1.15 '

USER_AGENTS = (
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',


    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; '
    '.NET CLR 3.0.04506)',

    'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR '
    '2.0.50727)',

    'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',

    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR '
    '3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',

    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; '
    '.NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)',

    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR '
    '3.0.04506.30)',

    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 ('
    'Change: 287 c9dfb30)',

    'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6',

    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1',

    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0',

    'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5',

    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',

    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',

    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 '
    'Safari/535.20',

    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 '
    'Safari/605.1.15',

    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',

)

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 10

CONCURRENT_REQUESTS_PER_DOMAIN = 1

COOKIES_ENABLED = False

TELNETCONSOLE_ENABLED = False

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}

SPIDER_MIDDLEWARES = {
}

DOWNLOADER_MIDDLEWARES = {
    'yelp_crawler.middlewares.HouseRentingAgentMiddleware': 100,
    # 'yelp_crawler.middlewares.HouseRentingProxyMiddleware': 200,
    'yelp_crawler.middlewares.HouseRentingRetryMiddleware': 300,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_crawlera.CrawleraMiddleware': 610
}

ITEM_PIPELINES = {
    'yelp_crawler.pipelines.HouseRentingPipeline': 100,
    'yelp_crawler.pipelines.DuplicatesPipeline': 200,
    'scrapy.pipelines.images.ImagesPipeline': 300,
    'yelp_crawler.pipelines.ESPipeline': 400,
}

IMAGES_STORE = '/yelp-crawler/data/images'

MEDIA_ALLOW_REDIRECTS = True

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 10
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 10
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 2.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = True

DOWNLOAD_TIMEOUT = 30
RETRY_TIMES = 3

# LOG_LEVEL = 'INFO'
LOG_LEVEL = 'DEBUG'

SPIDER_SETTINGS = {}

# ES 节点, 可以配置多个节点(集群), 默认为 None, 不会存储到 ES
ELASTIC_HOSTS = [
    {'host': 'elastic', 'port': 9200},
]

REDIS_HOST = 'redis'  # 默认为 None, 不会去重
REDIS_PORT = 6379  # 默认 6379

# SCRAPY_CRAWLERA
CRAWLERA_ENABLED = True
CRAWLERA_APIKEY = 'ed81328d71f243d6ba3c75e889e967f3'
CRAWLERA_PRESERVE_DELAY = 0
