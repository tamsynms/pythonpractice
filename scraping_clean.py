from bs4 import BeautifulSoup
from contextlib import closing
from urllib import request

url = "http://romandelarose.org"

html = request.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')
links = soup.find_all('a')[0:10]
links_html = soup.select('td.content a')

urls = []

for link in links_html:
    url = link['href'].replace('blob/', '')
    urls.append("https://raw.githubusercontent.com" + url)


corpus_texts = []

for url in urls:
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    text = soup.text.replace('\n', '')
    corpus_texts.append(text)

print(corpus_texts)
