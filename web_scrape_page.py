"""
description: webscrapes a single page
url is hardcoded
file: web_scrape_page.py
author: 
language: python 3.7

need to decompose this code to functions that can 
be used with import statement
"""
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# download the contents from the url
url = 'https://www.newegg.com/p/pl?N=100007709%20601296707'
response = requests.get(url)


# parse the webpage
soup = BeautifulSoup(response.text, "html.parser")


# search for all classes with class=item-container
containers = soup.findAll("div", {"class" : "item-container"})

# write info to csv file 'graphics_cards.csv'
filename = 'graphics_cards.csv'
f = open(filename, "w")

# add headers
headers = "brand, product_name, shipping, price\n"
f.write(headers)


# alright this does somthing like searching for each containter 
# i don't remember exactly how you just play with it a lil bit
# and figure it out bruh i know u r smart 
for container in containers:
	divItemInfo = container.find("div","item-info")
	brand = divItemInfo.a.img["title"]

	title_container = container.findAll("a", {"class" : "item-title"})
	product_name = title_container[0].text

	shipping_container = container.findAll("li", {"class" : "price-ship"})
	shipping = shipping_container[0].text.strip()

	price_container = container.findAll("li", {"class" : "price-current"})
	price = price_container[0].text.strip()
	final_price = price[2:9]

	print("Brand: " + brand)
	print("Product name: " + product_name)
	print("Shipping: " + shipping)
	print("Price: " + final_price)

	f.write(brand + "," + product_name.replace("," , "|") + "," + shipping + "," + final_price + "\n")

f.close