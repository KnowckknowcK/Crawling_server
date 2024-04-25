from trafilatura import feeds, fetch_url, extract
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env',
            verbose=True)

RSS_BASE_URL = os.getenv("RSS_BASE_URL")

feed_url = RSS_BASE_URL+"40300001/"

feed_list = feeds.find_feed_urls(feed_url)

for feed in feed_list[:2]:
    html = fetch_url(feed)
    text = extract(html)
    