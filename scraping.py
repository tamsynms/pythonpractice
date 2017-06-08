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
#take the HTML that we have a turn it into some soup (soup finds all the tags and stuff in the html) that we can work with
soup = BeautifulSoup(html, 'lxml')
#take all that soup and find all the anchor tags (the links)
links = soup.find_all('a')[0:10]
#go thourgh the soup and get all the text (first 2000 characters)
#print(soup.text[0:2000])
#print(soup.text.replace('\n', ' ')[0:1000])

#print(soup.select(".content"))

#links_html = soup.select('td.content a')
#urls = []
#for link in links_html:
#    url = link['href']
#    urls.append(url)
#print(urls)

#go through the soup, grab all the links that we care about (td tags with a content class that have a tag inside them)
links_html = soup.select('td.content a')
# make an empty list called urls
urls = []
#go through each url, get rid of 'blob/', and give me a link that adds the sub url to the base url. These will be links that actually work.
for link in links_html:
    url = link['href'].replace('blob/', '')
    urls.append("https://raw.githubusercontent.com" + url)
#print(urls)

#creates an empty list called corpus_texts
corpus_texts = []
#for each thing in urls, go through them
for url in urls:
    #print urls
    #print(url)
    #open the url and getting the htmlout of it
    html = request.urlopen(url).read()
    #convert html we have into something we can use -- a bunch of BeautifulSoup in this case
    soup = BeautifulSoup(html, "lxml")
    #get all the text from the soup that we have. then take all the line breaks and replace them with nothing.
    text = soup.text.replace('\n', '')
    # take the text data and add it to the growing corpus
    corpus_texts.append(text)
#print out the contents of the thing so you know that it ran
print(corpus_texts)
