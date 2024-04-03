import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from knowckknowck_crawling.items import Article
from bs4 import BeautifulSoup as bs



categories = {"101":"ECONOMICS",
              "100":"POLITICS",
              "102":"SOCIAL",
              "103":"ECONOMICS",
              "104":"ECONOMICS",
              "105":"IT",
              "106":"IT",
              "107":"IT",
              "108":"IT",
              "109":"IT"}


class CrawlerSpider(CrawlSpider):
    name = "url_crawler"
    allowed_domains = ["news.naver.com"]
    start_urls = ["https://news.naver.com/section/102"]


    def start_requests(self):
        for id in categories.keys():
            yield scrapy.Request("https://news.naver.com/section/"+id ,self.url_parse)
        
        

    def url_parse(self, response):
        columns = response.xpath('//div[@class="section_article as_headline _TEMPLATE"]/ul/li//*[@class="sa_text"]/a/@href')
        
        for column in  columns :
            print(column.get())
            yield scrapy.Request(column.get(),self.content_parse)




    def content_parse(self, response):
        item = Article()
        item['original_url']=response._get_url()
        print("10"+response._get_url()[-1])
        item['category']=categories["10"+response._get_url()[-1]]
        item['title']=response.xpath('//div[@class="media_end_head_title"]/h2/span/text()').get()
        item['created_at']=response.xpath('//div[@class="media_end_head_info_datestamp"]//span/@data-date-time').get()
        
        pre_content = response.xpath('//article[@class="go_trans _article_content"]').get()
        content = bs(pre_content, 'html.parser')
        content = content.select_one('#dic_area')

        for div in content.find_all('div'):
            div.clear()
        item['content']=content.get_text()


        yield item
