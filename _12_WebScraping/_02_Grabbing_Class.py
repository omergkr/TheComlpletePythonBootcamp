import requests
import bs4

"""
Syntax to pass to the .select()         Match Results

soup.select('div')                      All elements with the <div> tag

soup.select('#some_id')                 The HTML element containing the id attribute of some_id

soup.select('.notice')                  All the HTML elements with the CSS class named notice

soup.select('div span')                 Any elements named <span> that are within an element named <div>

soup.select('div > span')               Any elements named <span> that are directly within an element named <div>, 
                                        with no other element in between
"""

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text, "lxml")
# print(soup.select(".vector-toc-text"))

for element in soup.select(".vector-toc-text"):
    print(element.getText())
