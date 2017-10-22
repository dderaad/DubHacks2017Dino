# import libraries
# import urllib2
import urllib
from bs4 import BeautifulSoup

def scrape_asl_url(page_no, url):
    assert(len(page_no) >= 4)

    # query the website and return the html to the variable
    quote_page = 'https://www.handspeak.com/word/search/index.php?id='
    quote_page += str(page_no)
    quote_page = url
    print(quote_page)
    page = urllib.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser') # parsing the html using beautiful soup and store in variable

    print(soup)


scrape_asl_url("0001", 'http://secrets.rutgers.edu/dai/queryPages/search/result.php?type=partial&key=also&variant_name=ALSO&demonstrator=All&is_main=1')
