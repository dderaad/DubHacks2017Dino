# import libraries
# import urllib2
import urllib
import urllib.request as ur
from bs4 import BeautifulSoup
import os
#import lxml.html

#quote_page = 'http://secrets.rutgers.edu/dai/queryPages/search/result.php?type=partial&key=also&variant_name=' + gloss + '&demonstrator=All&is_main=1'

def scrape_asl_url(gloss_list):
    gtu = {}
    for gloss in gloss_list:
        quote_page = 'http://secrets.rutgers.edu/dai/queryPages/search/result.php?type=partial&key=also&variant_name={}&demonstrator=All&is_main=1'.format(gloss)
        #print(gloss)
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
        if len(tags)==0:
            gtu.pop(gloss, None)
        for tag in tags:
            url = tag.get('href')
            url = url[url.find('url=')+4:]
            gtu[gloss].add(url)

        print(gloss)


    return gtu


with open("glosses") as f:
    glosses = []
    for gloss in f:
        glosses.append(gloss.rstrip())


dict_is_made = False
for file in os.listdir("."):
    #is it already made?
    if file == "gloss_urls":
        dict_is_made = True
        break

if dict_is_made:
    #read dict from file
    with open("gloss_urls") as f:
        html_dict = {}
        for line in f:
            line = line.split(";")
            html_dict[line[0].rstrip()] = set(eval("set(" + line[1] + ")"))
else:
    html_dict = scrape_asl_url(glosses)


if not dict_is_made:
    #make the dictionary
    with open("gloss_urls", 'w') as f:
        for key in html_dict:
            f.write(key + ";" + str(html_dict[key]) + '\n')
