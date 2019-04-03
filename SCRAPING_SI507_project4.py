import requests, json
from bs4 import BeautifulSoup
from advanced_expiry_caching import Cache

START_URL = "https://www.nps.gov/index.htm"
FILENAME = "nps_cache.json"

PROGRAM_CACHE = Cache(FILENAME)

def access_page_data(url):
    data = PROGRAM_CACHE.get(url)
    if not data:
        data = requests.get(url).text
        PROGRAM_CACHE.set(url, data)
    return data



main_page = access_page_data(START_URL)

main_soup = BeautifulSoup(main_page, features="html.parser")
list_of_topics = main_soup.find('ul',{'class':'dropdown-menu SearchBar-keywordSearch'})

all_links = list_of_topics.find_all('a')

# print(all_links) # cool
# now need each one's href attr

# # Debugging/thinking code:
#
# for link in all_links:
#     print(link['href'])
#
#     # Just text! I'm not going back to the internet at all anymore since I cached the main page the first time

# This is stuff ^ I'd eventually clean up, but probably not at first as I work through this problem.

topics_pages = [] # gotta get all the data in BeautifulSoup objects to work with...
for l in all_links:
    page_data = access_page_data('https://www.nps.gov' + l['href'])
    soup_of_page = BeautifulSoup(page_data, features="html.parser")
    # print(soup_of_page)
    topics_pages.append(soup_of_page)

# Now I can do some investigation on just one of those BeautifulSoup instances, and thus decide what I want to do with each one...
# Each time I run the program, I'm not going to the internet at all sometimes unless some page is new or it's -- in this case -- been more than 7 days since storing data.
# After the first time, it'll run much faster! (On a certain scale, anyway)

# Just for example --
# print(topics_pages[0].prettify())
