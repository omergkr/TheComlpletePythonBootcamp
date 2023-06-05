import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text, "lxml")
image_info = soup.select("a.image img")
print(image_info[0])
computer = soup.select("a.image img")[0]
print(type(computer["src"]))
image_link = requests.get("https:" + computer["src"])
print(image_link.content)
f = open("C:\\Users\\ÖmerGöker\\Desktop\\my_computer_image.jpg", "wb")
f.write(image_link.content)
f.close()

