# Doing the necessary imports

import requests
from bs4 import BeautifulSoup
import re
import csv
import sys

boat_listing_request = "http://www.boattrader.com/search-results/NewOrUsed-any/Type-all/Zip-94555/Radius-4000/Sort-Length:DESC"

boat_results = requests.get(boat_listing_request)

raw_html_boat_results = boat_results.text

bs = BeautifulSoup(raw_html_boat_results,'html.parser')

first_result_page = bs.find_all('div',{'class':'ad-title'}) # This is the list you will pass to the function at the very begining.

# Find the total number of listings for that search.

search_count = bs.find_all('div',{'class':'search-viewing'})

raw_count_string = search_count[0].text.lstrip().rstrip()

m = re.search('of(.+?)Listings', raw_count_string)
if m:
    found = m.group(1)

total_result_count_value = int(found.lstrip())

print "Total search results count is: " + str(total_result_count_value)

# Open the flat csv file and insert the header record into it.

f = open(sys.argv[1], 'wt')
try:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow( ('Boat Make', 'Boat Model','Boat Price','URL_Link', 'Seller Name', 'Seller Phone number') )
finally:
    f.close()

# Define the function that will take the list of the individual results with link, and scrap the much needed information,
# only to be inserted into the csv file.

def scrap_individual_result(my_list):
	length_of_list = len(my_list)

	for num in range(length_of_list):
		individual_result_link = 'http://www.boattrader.com' + my_list[num].a['href']
		request_indi_link = requests.get(individual_result_link)
		request_text_indi_link = request_indi_link.text
		new_soup = BeautifulSoup(request_text_indi_link,'html.parser')
		# Find seller
		find_seller = new_soup.find_all('div',{'class':'seller-details'})
		try:
			seller_name = find_seller[0].h4.text
		except IndexError as e:
			seller_name = "Error in the seller name found"
		# Seller phone number
		find_seller_phone = new_soup.find_all('div',{'class':'phone'})
		final_seller_number = find_seller_phone[0].text
		# Make of the boat
		find_bd_make = new_soup.find_all('span',{'class':'bd-make'})
		final_boat_make = find_bd_make[0].text
		# Model of the boat
		find_bd_model = new_soup.find_all('span',{'class':'bd-model'})
		final_boat_model = find_bd_model[0].text
		# Price of the boat
		find_bd_price = new_soup.find_all('span',{'class':'bd-price'})
		price_value_in_list = find_bd_price[0].text.replace(" ","").lstrip()
		# Appending all of these variables to the text csv file
		f = open(sys.argv[1], 'a')

		try:
			writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
			writer.writerow( (final_boat_make,final_boat_model,price_value_in_list,individual_result_link,seller_name,final_seller_number) )
		finally:
			f.close()


scrap_individual_result(first_result_page)

result_counter = 25

while (result_counter < 800):
	# Find the code for going to the next page after extracting the first 25 records of the current search

	find_next_page = bs.find_all('a', {'title':'Next Page'})
	next_button_link = 'http://www.boattrader.com' + find_next_page[0]['href']
	print next_button_link
	next_click = requests.get(next_button_link)
	raw_html_boat_result = next_click.text
	bs = BeautifulSoup(raw_html_boat_result,'html.parser')
	result_pages = bs.find_all('div',{'class':'ad-title'})
	scrap_individual_result(result_pages)
	result_counter += 25

print "The scraper has completed scraping the boat trader website for 800 records of links. Check the file test.csv out"


