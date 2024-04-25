from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import time


def excute():
    process = CrawlerProcess(get_project_settings())
    process.crawl('naver_news_crawler')
    process.start()

if __name__=='__main__':
    excute()