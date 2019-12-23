from urllib.request import urlopen
from selenium import webdriver
import webbrowser
import re

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

product = input("The name of the product: ")
URL = "https://www.emag.hu/search/"+product


pages = []
for i in range(1, 11):
    page_edit = URL + "/p" + str(i)
    pages.append(page_edit)

price_list = []
hrefs = []


def priceConv(price):
    x = re.sub("\\D", "", price)
    price_list.append(int(x))


def hrefList(href):
    hrefs.append(href)


for page in pages:
    driver.get(page)
    for i in driver.find_elements_by_class_name("card-item"):
        raw_price = i.find_element_by_class_name("product-new-price").text
        if len(raw_price) > 2:
            priceConv(raw_price)
            hrefList(i.find_element_by_css_selector('a').get_attribute('href'))
        else:
            pass


for i in price_list:
    cheapest = min(price_list)

index = price_list.index(cheapest)
webbrowser.open(hrefs[index])
print(f"A legolcsobb termek ara: {cheapest}Ft.")
