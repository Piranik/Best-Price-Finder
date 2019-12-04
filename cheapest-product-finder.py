from urllib.request import urlopen
from bs4 import BeautifulSoup, SoupStrainer
import webbrowser
import re

product = input("The name of the product: ")
URL = "https://www.emag.hu/search/"+product
html = BeautifulSoup(urlopen(URL), "html5lib")


prices = html.find_all("p", class_="product-new-price")
price_list = []


for i in prices:
    if len(i) < 2:
        pass
    else:
        price = re.sub("\D", "", i.get_text())
        price_list.append(int(price))


for i in price_list:
    cheapest = min(price_list)
    index = price_list.index(cheapest)


def open(index):
    href = html.find_all(
        "a", class_="product-title js-product-url")[index]["href"]
    webbrowser.open(href)
    print(href)


open(index)
print(f"A legolcsobb termek ara: {cheapest}Ft.")
print(price_list)
