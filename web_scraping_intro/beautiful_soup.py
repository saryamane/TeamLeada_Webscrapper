import requests
from bs4 import BeautifulSoup, SoupStrainer

search_link = "http://sfbay.craigslist.org/search/sss?query=motorcycles&sort=rel"

r = requests.get(search_link)
raw_html = r.text

# No one likes raw HTML document, we need this properly formatted.

# The returned HTML is nearly incomprehensible. This is where BeautifulSoup comes into picture.

# Start by creating a BeautifulSoup object

soup = BeautifulSoup(raw_html,'html.parser')

# Use the find_all method to query the response returned from the HTML parsed well by the BeautifulSoup

search_results = soup.find_all('a', {'class': 'i'})

# Print only the first search results

print search_results[0] # printint the first element.

# we just need the content of the href element.

print search_results[0]['href']

# Print the value of the data-id of the 3rd element returned by BeautifulSoup parser.

print search_results[2]['data-id']

