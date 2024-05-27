import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from knowckknowck_crawling.items import Article
from bs4 import BeautifulSoup as bs
from trafilatura import feeds, fetch_url, extract
from datetime import datetime
import logging
import re



categories = {"30300018":"ECONOMICS",
              "50200011":"ECONOMICS",
              "30200030":"POLITICS",
              "50400012":"SOCIAL",
              "30300018":"WORLD",
              "30000023":"ENTERTAINMENT",
              "71000001":"SPORT",
              }


logging.basicConfig(filename="../../crawling.log", level=logging.DEBUG, 
                    format="[ %(asctime)s | %(levelname)s ] %(message)s", 
                    datefmt="%Y-%m-%d %H:%M:%S")
logger2 = logging.getLogger()

class CrawlerSpider(CrawlSpider):
    name = "rss_crawler"
    allowed_domains = ["www.mk.co.kr"]
    start_urls = ["https://www.mk.co.kr/rss/"]



    def start_requests(self):
        for id in categories.keys():
            yield scrapy.Request("https://www.mk.co.kr/rss/"+id,
                                 self.url_parse)
        
        

    def url_parse(self, response):
        feed_url = response._get_url()
        feed_list = feeds.find_feed_urls(feed_url)
        
        for feed in feed_list[:3]:
            logger2.info(feed)
            yield scrapy.Request(feed,
                                 self.content_parse,
                                 meta={'category':feed_url[-8:]})



    def content_parse(self, response):
        item = Article()

        feed = response._get_url()
        item['id']=int(feed[-8:])
        item['original_url']=feed
        item['category']=categories[response.meta['category']]
        
        created_at = response.xpath('//div[@class="time_area"]//dd/text()').get()
        item['created_at']=created_at

        pre_title = response.xpath('//div[@class="txt_area"]/h2[@class="news_ttl"]/text()').get()
        pre_title = pre_title.replace("\'","").replace("\"","").replace("...","").replace("…","").replace("’","").replace("‘","").replace("”","").replace("“","")
        pattern = r'\[[^]]*\]'
        title = re.sub(pattern=pattern, repl='', string=pre_title)    
        item['title']=title if title[0]!=' ' else title[1:]
        
        
        html = fetch_url(feed)
        text = extract(html)
        item['content']=text


        yield item

