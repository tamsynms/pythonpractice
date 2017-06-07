#get all the libraries that we want
from bs4 import BeautifulSoup
from contextlib import closing
from urllib import request

#stores base url for our site
url = "https://github.com/humanitiesprogramming/scraping-corpus"

#print(url)

#print(url + "/subdomain")

#using that url, get the HTML from it.
html = request.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')
links = soup.find_all('a')[0:10]

print(soup.text[0:2000])
#print(soup.text.replace('\n', ' ')[0:1000])

#print(soup.select(".content"))

#links_html = soup.select('td.content a')
#urls = []
#for link in links_html:
#    url = link['href']
#    urls.append(url)
#print(urls)

links_html = soup.select('td.content a')
urls = []
for link in links_html:
    url = link['href'].replace('blob/', '')
    urls.append("https://raw.githubusercontent.com" + url)
print(urls)

corpus_texts = []
for url in urls:
    print(url)
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    text = soup.text.replace('\n', '')
    corpus_texts.append(text)

print(corpus_texts)
