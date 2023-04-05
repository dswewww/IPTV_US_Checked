import requests
import urllib.request
from bs4 import BeautifulSoup
import wget
URL = "https://youshandefeiyang.github.io/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("code")
cnt = 0
for tag in results:

    url = tag.text.strip().replace(" ","")
    if url.startswith("http"):
        print(url)
        print(tag.next_sibling.strip())
        import requests

        headers = {'User-Agent': 'Mozilla/5.0'}

        r = requests.get(url, headers=headers)
        # print(r.content)

        with open(str(cnt)+".m3u", 'wb') as fh:
            fh.write(r.content)
        cnt += 1

