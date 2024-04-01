from fastapi import FastAPI
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import time

app = FastAPI()

@app.get("/",)
async def post_articles():
    
    process = CrawlerProcess(get_project_settings())
    process.crawl('url_crawler')
