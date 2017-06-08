from bs4 import BeautifulSoup
from contextlib import closing
from urllib import request

url = "https://raw.githubusercontent.com/humanitiesprogramming/scraping-corpus/master/full-text.txt"
html = request.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')
raw_text = soup.text
texts = eval(soup.text)

print(len(raw_text))
print(len(texts))
print(texts)
