# Step 1. Do all the imports from before (requests and BeautifulSoup).

import requests
from bs4 import BeautifulSoup, SoupStrainer

# Step 2. Now start at the first search result page (manually grab the url). 

my_search_result = 'http://sfbay.craigslist.org/search/zip?query=sofa'

r = requests.get(my_search_result)

search_result_pg = r.text

# Step 3. Build a BeautifulSoup object on the returned html.

soup = BeautifulSoup(search_result_pg, 'html.parser')

# For each link that leads to an individual ad listing, visit the link, build a BuiltifulSoup object, 
# and extract whatever you want (we did the page title before).

all_result_links = soup.find_all('a', {'class':'i'})

total_count = soup.find_all('span',{'class':'totalcount'})
total_count_value = int(total_count[0].text)

print total_count_value

# print all_result_links[0]['href'] # This will print now each of the links present in the search results page.

def visit_links(all_result_links, counter_value):

	len_list = len(all_result_links)

	for num in range(len_list):
		indi_result = 'http://sfbay.craigslist.org' + all_result_links[num]['href']
		q = requests.get(indi_result)
		raw_indi_result = q.text
		bs = BeautifulSoup(raw_indi_result,'html.parser')
		extract_title = bs.find_all('h2', {'class':'postingtitle'})
		print extract_title[0].text.rstrip()
		print
		extract_body = bs.find_all('section', {'id': 'postingbody'}) 
		print extract_body[0].text.rstrip()

	print "I am done printing all the output titles..now find the Next button on the search result page and click it: " + str(counter_value)

visit_links(all_result_links, 0)

pg_counter = 100

while(pg_counter < total_count_value):

	find_next_button = soup.find_all('a',{'class':'button next'})

	next_link = 'http://sfbay.craigslist.org' + find_next_button[0]['href']
	print next_link
	next_click = requests.get(next_link)

	raw_html_next_click =  next_click.text
	soup = BeautifulSoup(raw_html_next_click,'html.parser')

	next_all_results = soup.find_all('a', {'class':'i'})

	visit_links(next_all_results, pg_counter)
	pg_counter += 100

print " The scrapper has resturned you all the results and now the web scraping program has now ended!"




