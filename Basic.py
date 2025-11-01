from spider import Spider
import os
import json
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

def encode_url(url):
    return urlparse(url).netloc

app = Spider()
# possible modes aare smart, http, and chrome.
params = {"limit":2, "return_format": "markdown", "request": "smart"}
crawl_result = app.crawl_url('https://hulu.com', params=params)

print(crawl_result)

# the first result in the crawl result is it is not empty pull it by the 'url' key
filename = crawl_result[0]['url']
if filename:
    # encode the url safely to store as a filename
    filename = encode_url(filename)
else:
    print("No URL found")

os.makedirs('data', exist_ok=True)
with open(f'data/level_1/{filename}.json', 'w') as f:
    json.dump(crawl_result, f)
    