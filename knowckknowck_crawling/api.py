from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import time


def api():
    process = CrawlerProcess(get_project_settings())
    process.crawl('url_crawler')
    process.start()

if __name__=='__main__':
    api()