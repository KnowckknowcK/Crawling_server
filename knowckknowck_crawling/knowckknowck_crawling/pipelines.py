# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path='../.env',
            verbose=True)

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_SCHEMA = os.getenv("DB_SCHEMA")


class KnowckknowckDataPipeline:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = DB_HOST,
            user = DB_USER,
            password = DB_PASSWORD,
            database = DB_SCHEMA
        )
        self.cur = self.conn.cursor()

    def process_item(self,item,spider):
        self.cur.execute(""" insert into article (id,created_time,article_url,category,title,content) values (%s,%s,%s,%s,%s,%s)""", (
            item["id"],
            item["created_at"],
            item["original_url"],
            item["category"],
            item["title"],
            item["content"],
        ))
        self.conn.commit()

    def close_spider(self, spider):

        self.cur.close()
        self.conn.close()


class KnowckknowckCrawlingPipeline:
    def process_item(self, item, spider):
        return item
