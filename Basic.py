from spider import Spider
import os
import json
from dotenv import load_dotenv
from urllib.parse import urlparse
from datetime import datetime

load_dotenv()

def encode_url(url):
    return urlparse(url).netloc

app = Spider()

url = 'https://www.wikipedia.org'
# possible modes aare smart, http, and chrome.
params = {"limit":2, "return_format": "markdown", "request": "smart"}
crawl_result = app.crawl_url(url, params=params)

print(crawl_result)

# the first result in the crawl result is it is not empty pull it by the 'url' key
filename = crawl_result[0]['url']
if filename:
    # encode the url safely to store as a filename
    filename = encode_url(filename)
else:
    print("No URL found")

# help me parse the domain from the url
domain =  urlparse(url).hostname

os.makedirs(f'data/level_1/{domain}', exist_ok=True)

# add the date with the date + filename
date_str = datetime.now().strftime('%Y-%m-%d')
filename_with_date = f'{date_str}_{filename}'

with open(f'data/level_1/{domain}/{filename_with_date}.json', 'w') as f:
    json.dump(crawl_result, f)
    #