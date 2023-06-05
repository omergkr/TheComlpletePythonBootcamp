# Goal : get tittle of every book with a 2 star rating

import requests
import bs4

# https://books.toscrape.com/catalogue/page-2.html

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
# res = requests.get(base_url.format(1))
# soup = bs4.BeautifulSoup(res.text, "lxml")
# products = soup.select(".product_pod")
# example = products[0]
# print(example)
# print([] == example.select(".star-rating.Two"))
# print(example.select("a")[1]["title"])

two_star_titles = []

for n in range(1, 51):
    res = requests.get(base_url.format(n))
    soup = bs4.BeautifulSoup(res.text, "lxml")
    books = soup.select(".product_pod")
    for book in books:
        # if "star-rating Two" in str(book):
        if len(book.select(".star-rating.Two")) != 0:
            book_title = book.select("a")[1]["title"]
            print(book_title)
            two_star_titles.append(book_title)






