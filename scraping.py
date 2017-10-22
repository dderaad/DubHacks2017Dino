# import libraries
# import urllib2
import urllib
import urllib.request as ur
from bs4 import BeautifulSoup
import lxml.html

glosses = ['ALSO']
#quote_page = 'http://secrets.rutgers.edu/dai/queryPages/search/result.php?type=partial&key=also&variant_name=' + gloss + '&demonstrator=All&is_main=1'

def scrape_asl_url(gloss_list):
    gtu = {}
    for gloss in gloss_list:
        quote_page = 'http://secrets.rutgers.edu/dai/queryPages/search/result.php?type=partial&key=also&variant_name={}&demonstrator=All&is_main=1'.format(gloss)
        print(gloss)
        page = ur.urlopen(quote_page)
        soup = BeautifulSoup(page, 'html.parser') # parsing the html using beautiful soup and store in variable

        #print(soup)
        """
        for link in soup.find_all('a'):
            links = (link.get('href'))
            print(links)
            return links
        """
        gtu[gloss] = set()
        tags = soup.find_all('a')
        for tag in tags:
            url = tag.get('href')
            url = url[url.find('url=')+4:]
            gtu[gloss].add(url)


    return gtu


with open("glosses") as f:
    glosses = []
    for gloss in f:
        glosses.append(gloss.rstrip())

html_dict = scrape_asl_url(glosses)
print(html_dict)
