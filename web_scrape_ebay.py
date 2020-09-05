"""
description: This application collects data from ebay based on the search request:
e.g. request such as "Honda Accord" will collect all the data (model, year of manufacturing,
price, mileage) related to this make and model and write it to a csv file.

author: Raman Zatsarenko rzv0907101@gmail.com
"""


import requests
from bs4 import BeautifulSoup


def get_url():
	"""
	creates a url for a given vehicle from the input
	"""
	make = input("Please enter the vehicle manufacturer: ")
	model = input("Please enter the vehicle model: ")
	# make = "ford"
	# model = "mustang"
	url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2499334.m570.l2632&_nkw=" \
		  + make + "+" + model + "&_sacat=6001"
	return url


def parse_page(url):
	"""
	Parses the webpage into a BS object
	"""
	response = requests.get(url)

	# parse the webPage

	webPage = BeautifulSoup(response.text, "html.parser")

	return webPage


def create_csv():
	"""
	creates csv file containing info
	scrapped from a single webpage
	"""
	filename = "vehicle_info.csv"

	f = open(filename, "w")
	# inspect the html code and add headers strings to the following variable

	headers = "Vehicle_Type,Year,Price,Mileage\n"
	f.write(headers)

	return f


def get_and_write_info(webPage, file):
	"""
	writes all the necessary info to a csv file
	:param webPage: webpage in a form of BS object
	:param file: file to be written to
	:return: None
	"""

	containers = webPage.findAll("div", {"class": "s-item__info clearfix"})
	for container in containers:
		vehicle_a = container.find("a")
		vehicle_info = vehicle_a.h3.find_all("span")
		if vehicle_info == []:
			vehicle_info = vehicle_a.h3.contents[-1]
		else:
			vehicle_info = vehicle_info[-1].contents[-1]
			if vehicle_info == "New Listing":
				vehicle_info = vehicle_a.h3.contents[-1]

		# get vehicle price

		divPrice = container.find("div", "s-item__detail s-item__detail--primary")
		#print(divPrice.span.contents[0])

		price = divPrice.find_all("span")[-1].contents[0].split(",")
		print(price)

		#price = divPrice.span.contents[0].split(",")
		if len(price) == 1:
			pos = 0
			# delete dot from price for easier data processing
			for ch in price[0]:
				if ch == '.':
					no_dot_price = price[0][:pos]
					break
				pos+=1
			formatted_price = no_dot_price
		else:
			# delete dot from the price for easier data processing
			pos = 0
			for ch in price[1]:
				if ch == '.':
					no_dot_price = price[1][:pos]
					break
				pos+=1
			formatted_price = price[0] + no_dot_price

		# slice vehicle info string

		year = vehicle_info[:4]
		make_model = vehicle_info[5:]

		spanMileage = container.find("span", "s-item__dynamic s-item__dynamicAttributes2")
		if spanMileage is None:
			pass
		else:
			mileage = spanMileage.contents[0][6:]
			if len(mileage) > 4:
				temp_mileage = mileage.split(",")
				mileage = temp_mileage[0] + temp_mileage[1]

		file.write(make_model.split(",")[0] + "," + year + "," + formatted_price + "," + mileage + "\n")
		print(make_model)
		print([vehicle_info, formatted_price, mileage])


def find_page_numbers(webPage):
	"""
	finds a number of pages for a given search request
	:param webPage: parse tree, soup object
	:return: list containing all numbers of pages
	"""
	liPages = webPage.findAll("a", {"class" : "pagination__item"})

	# insert the page numbers to the array based on the len of liPages list
	pages = [i for i in range(1, len(liPages) + 1)]

	print(pages)
	return pages


def get_pages(webPage, url, file):
	"""
	analyzes multiple pages for a given search request
	if pages is empty analyzes a single page
	:param pages: list of pages
	:return: none
	"""
	pages = find_page_numbers(webPage)
	if not pages:
		get_and_write_info(webPage, file)
	else:
		for page in pages:
			current_url = url + "&_pgn=" + str(page)
			soup = parse_page(current_url)
			get_and_write_info(soup, file)
	file.close()



def test(webPage):
	"""
	a testing function for create csv
	:param webPage: webPage to be scraped
	:return: none
	THIS CODE IS WORKING CHANGE create_csv USING THIS
	"""
	containers = webPage.findAll("div", {"class": "s-item__info clearfix"})
	count = 0
	for container in containers:
		vehicle_a = container.find("a")
		vehicle_info = vehicle_a.h3.find_all("span")
		if vehicle_info == []:
			vehicle_info = vehicle_a.h3.contents[-1]
		else:
			vehicle_info = vehicle_info[-1].contents[-1]
			if vehicle_info == "New Listing":
				vehicle_info = vehicle_a.h3.contents[-1]
		count+= 1
		print(vehicle_info)
	print(count)


def main():
	"""
	main function gets the url from user input,
	creates a BS object, parses it, gets all the necessary data
	and writes it to a сsv
	:return: None
	"""
	url = get_url()
	print(url)
	soup = parse_page(url)
	file = create_csv()
	get_pages(soup, url, file)


if __name__ == '__main__':
	main()