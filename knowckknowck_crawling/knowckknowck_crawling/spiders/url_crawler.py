import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from knowckknowck_crawling.items import Article

class CrawlerSpider(CrawlSpider):
    name = "url_crawler"
    allowed_domains = ["news.naver.com"]
    start_urls = ["https://news.naver.com/section/102"]


    def start_requests(self):
        yield scrapy.Request("https://news.naver.com/section/102",self.parse)

    def parse(self, response):
        items = []
        columns = response.xpath('//div[@class="section_article as_headline _TEMPLATE"]/ul/li//*[@class="sa_text"]/a/@href')
        
        for column in  columns :
            item = Article()
            item['original_url'] = column.get()
            items.append(item)
        
        return items        