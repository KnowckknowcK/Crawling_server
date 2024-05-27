import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from knowckknowck_crawling.items import Article
from bs4 import BeautifulSoup as bs
from datetime import datetime
import logging
import re



categories = {"100":"POLITICS",
              "101":"ECONOMICS",
              "102":"SOCIAL",
              "103":"CULTURE",
              "104":"WORLD",
              "105":"IT",
              "106":"ENTERTAINMENT",
              "107":"SPORT",
              "108":"SOCIAL",
              "109":"SOCIAL"}


logging.basicConfig(filename="../../crawling.log", level=logging.DEBUG, 
                    format="[ %(asctime)s | %(levelname)s ] %(message)s", 
                    datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger()

class CrawlerSpider(CrawlSpider):
    name = "naver_news_crawler"
    allowed_domains = ["news.naver.com"]
    start_urls = ["https://news.naver.com/section/102"]


    def start_requests(self):
        for id in categories.keys():
            yield scrapy.Request("https://news.naver.com/section/"+id ,self.url_parse)
        
        

    def url_parse(self, response):
        columns = response.xpath('//div[@class="section_article as_headline _TEMPLATE"]/ul/li//*[@class="sa_text"]/a/@href')
        
        for column in  columns :
            logger.info(column.get())
            yield scrapy.Request(column.get(),
                                 self.content_parse,
                                 meta={'category':response._get_url()[-3:]})




    def content_parse(self, response):
        item = Article()
        url = response._get_url()
        item['id']=int(url[-10:])
        item['original_url']=url
        item['category']=categories[response.meta['category']]
        item['created_at']=response.xpath('//div[@class="media_end_head_info_datestamp"]//span/@data-date-time').get()

        pre_title = response.xpath('//div[@class="media_end_head_title"]/h2/span/text()').get()
        pre_title = pre_title.replace("\'","").replace("\"","").replace("..."," ").replace("…"," ").replace("’","").replace("‘","").replace("”","").replace("“","")
        pattern = r'\[[^]]*\]'
        title = re.sub(pattern=pattern, repl='', string=pre_title)    
        item['title']=title if title[0]!=' ' else title[1:]
        
        pre_content = response.xpath('//article[@class="go_trans _article_content"]').get()
        content = bs(pre_content, 'html.parser')
        content = content.select_one('#dic_area')

        for div in content.find_all('div'):
            div.clear()
        item['content']=content.get_text()


        yield item
