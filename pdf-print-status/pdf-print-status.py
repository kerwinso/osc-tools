import urllib
# Install BS4 first:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup
from bs4 import BeautifulSoup

inputfile = 'IDs.txt'
idlist = open(inputfile)

#stmsgs = []

for each in idlist:
  collID = each.strip()
  url = 'http://legacy.cnx.org/content/col'+collID+'/latest/printinfo'
  html = urllib.urlopen(url).read()
  soup = BeautifulSoup(html, "lxml")
  for s in soup.find_all('div','status'):
    span = s.find('span','data')
    status = span.string
    statusmsg = "Process status for col" + collID + ": " + status
    print statusmsg
 #   stmsgs.append(statusmsg)

#print len(stmsgs)