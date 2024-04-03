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

HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")


class KnowckknowckDataPipeline:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = HOST,
            user = USER,
            password = PASSWORD,
            database = DATABASE
        )
        self.cur = self.conn.cursor()

    def process_item(self,item,spider):
        self.cur.execute(""" insert into article (article_url) values (%s)""", (
            item["original_url"],
        ))
        self.conn.commit()

    def close_spider(self, spider):

        self.cur.close()
        self.conn.close()


class KnowckknowckCrawlingPipeline:
    def process_item(self, item, spider):
        return item
