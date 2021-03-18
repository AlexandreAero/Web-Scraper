import requests
import string

from collections import Counter

from bs4 import BeautifulSoup


url = "https://bbc.com/news"


response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
links = soup.findAll("a")

news_urls = []
for link in links:
    href = link.get("href")
    if href.startswith("/news") and href[-1].isdigit():
        news_url = "https://bbc.com" + href
        news_urls.append(news_url)


all_nouns = []
for url in news_urls[:10]:
    print("Fetching {}".format(url))
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    words = soup.text.split()
    nouns = [word for word in words if word.isalpha() and word[0] in string.ascii_uppercase]
    all_nouns += nouns

print(Counter(all_nouns).most_common(100))