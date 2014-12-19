import requests
from bs4 import BeautifulSoup

example_listing = 'http://sfbay.craigslist.org/scz/sys/4810341652.html'

r = requests.get(example_listing)

ad_page_html = r.text

soup = BeautifulSoup(ad_page_html,'html.parser')

title = soup.find_all('h2', {'class':'postingtitle'})

# print title[0].contents[2].rstrip()

print title[0].text # Solution provided to me by Tristan.

# print title[0].contents[2] # This is the solution that also works.

# def picklines(thetext, whatlines):
#   return [x for i, x in enumerate(thetext) if whatlines not in x]

# title_value = picklines(text_value, '<')
# print title_value[2]

# Let's proceed to execute the next button programmatically.

user_search = 'http://sfbay.craigslist.org/search/sss?query=macbook&sort=rel'
p = requests.get(user_search)
search_pg_html = p.text
search_soup = BeautifulSoup(search_pg_html,'html.parser')

# <a href="/search/sss?s=100&amp;query=macbook&amp;sort=rel" class="button next" title="next page"> next &gt; </a>

next_button = search_soup.find_all('a', {'class':'button next'})
print len(next_button)
print next_button

uniq_button = set(next_button)
print uniq_button
print len(uniq_button)

