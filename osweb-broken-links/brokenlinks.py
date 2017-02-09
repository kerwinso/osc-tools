"""
Check for broken links on the OS QA website.
"""
import requests
import urllib
from bs4 import BeautifulSoup

address = 'http://oscms-qa.openstax.org/sitemap.xml'
xml = urllib.urlopen(address).read()
print ("Retrieving sitemap from " + address + ", processing...")

soup = BeautifulSoup(xml, 'lxml')

links = []
qalinks = []

# gather all the links from the sitemap.xml into a list
for s in soup.find_all('loc'):
    links.append(s.text)

# rewrite those links to use the QA domain and put into another list
for link in links:
    newlink = link.replace('openstax.org', 'oscms-qa.openstax.org')
    qalinks.append(newlink)

broken_links = []
for link in qalinks:
    r = requests.get(link)
    status = r.status_code
    if status != 200:
        print ('Error code ' + str(status) + ' found on: ' + link)
        broken_links.append(link)
    else:
        print (link + ': OK')

print('Number of broken links: ' + str(len(broken_links)))

if len(broken_links) > 0:
    print('List of broken links: ')
    for link in broken_links:
        print ('\t' + link)
