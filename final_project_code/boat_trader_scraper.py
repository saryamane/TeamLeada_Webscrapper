# Making the necessary imports for the web scraper project.

import requests
from bs4 import BeautifulSoup
import re
import csv
import sys

boat_listing_request = "http://www.boattrader.com/search-results/NewOrUsed-any/Type-all/Zip-94555/Radius-4000/Sort-Length:DESC"

boat_results = requests.get(boat_listing_request)

raw_html_boat_results = boat_results.text

bs = BeautifulSoup(raw_html_boat_results,'html.parser')

first_result = bs.find_all('div',{'class':'ad-title'})

# Find the total number of listings for that search.

search_count = bs.find_all('div',{'class':'search-viewing'})

raw_count_string = search_count[0].text.lstrip().rstrip()

m = re.search('of(.+?)Listings', raw_count_string)
if m:
    found = m.group(1)

total_result_count_value = int(found.lstrip())

print "Total search results count is: " + str(total_result_count_value)

# Find the code for going to the next page after extracting the first 25 records of the current search.

find_next_page = bs.find_all('a', {'title':'Next Page'})
next_button_link = 'http://www.boattrader.com' + find_next_page[0]['href']
print next_button_link

# print first_result[0].text

# Find the URL for each and every boat being listed on the entire website

result_page = 'http://www.boattrader.com' + first_result[0].a['href']

# print 'http://www.boattrader.com' + first_result[0]['href']

new_result_html = requests.get(result_page)

final_result = new_result_html.text

new_soup = BeautifulSoup(final_result,'html.parser')

# find_make = new_soup.find_all('tbody')

# my_table = find_make[0]

# rows = my_table.findChildren(['th', 'td'])

# print "Make of the boat is: " + rows[7].text # This gets the make of the ship.

# Let's print the sellers information now.

find_seller = new_soup.find_all('div',{'class':'seller-details'})

seller_name = find_seller[0].h4.text

print "Seller Name is: " + seller_name

find_seller_phone = new_soup.find_all('div',{'class':'phone'})
final_seller_number = find_seller_phone[0].text
print "Seller's phone number is: " + find_seller_phone[0].text

# Another way to get the make, model and price of the boat result is using the bd values within the inidvidual search result.

# Find the make of the boat from the individual result page.

find_bd_make = new_soup.find_all('span',{'class':'bd-make'})
final_boat_make = find_bd_make[0].text
print "The make of the ship is: " + find_bd_make[0].text

# Find the model of the boat from the individual result page.

find_bd_model = new_soup.find_all('span',{'class':'bd-model'})
final_boat_model = find_bd_model[0].text
print "The model of the ship is: " + find_bd_model[0].text

# Find the price of the boat from the individual result page.

find_bd_price = new_soup.find_all('span',{'class':'bd-price'})
price_value_in_list = find_bd_price[0].text.replace(" ","").lstrip()
print "The price of the boat is: " + price_value_in_list


# Writing all this to the csv file.

f = open(sys.argv[1], 'wt')
try:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow( ('Boat Make', 'Boat Model','Boat Price','URL_Link', 'Seller Name', 'Seller Phone number') )
    # for i in range(10):
    #     writer.writerow( (i+1, chr(ord('a') + i), '08/%02d/07' % (i+1)) )
finally:
    f.close()

# Insert now the data elements into the flat file.
f = open(sys.argv[1], 'a')

try:
	writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
	writer.writerow( (final_boat_make,final_boat_model,price_value_in_list,result_page,seller_name,final_seller_number) )
finally:
	f.close()


print open(sys.argv[1], 'rt').read()
