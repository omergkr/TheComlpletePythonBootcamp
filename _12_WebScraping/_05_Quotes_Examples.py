import requests
import bs4

# http://quotes.toscrape.com/


res = requests.get("http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(res.text, "lxml")
title = soup.select("title")
print(title)
authors = set()
for name in soup.select(".author"):
    authors.add(name.text)

print(authors)

quotes = []
for quote in soup.select("span.text"):
    quotes.append(quote.text)

print(quotes)

top_ten_tags = []
for tag in soup.select("span.tag-item>a"):
    top_ten_tags.append(tag.text)

print(top_ten_tags)


url = 'http://quotes.toscrape.com/page/'

authors_set = set()
for page in range(1, 10):
    page_url = url + str(page)
    res = requests.get(page_url)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    for name in soup.select(".author"):
        authors_set.add(name.text)


print(authors_set)
print(len(authors_set))

search_on = True
page = 1
while search_on:
    page_url = url + str(page)
    res = requests.get(page_url)
    if "No quotes found!" in res.text:
        break
    for name in soup.select(".author"):
        authors.add(name.text)
    page += 1

print(authors_set)
