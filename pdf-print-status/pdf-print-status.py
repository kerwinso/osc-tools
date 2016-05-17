import urllib
import datetime
# Install BS4 first:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup
from bs4 import BeautifulSoup
#install yagmail first: pip install yagmail or easy_install yagmail
import yagmail

# List of email recipients must be formatted like this: 
# ['email1@host.com','email2@host.com']
to = ['ks52@rice.edu', 'brw5@rice.edu']

# Email notification; only gets called if there's an un-locked PDF on production
def ymail():
    pdflist = "\n".join(unlocked)
    fullstatuslist = '\n'.join(stmsgs)
    timestamp = '{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())
    today = datetime.date.today()    
    # the Gmail user is the parameter for yagmail.SMTP
    yag = yagmail.SMTP('oscontentqa')
    contents = [
        'PDFs that are not locked on production as of '+ str(timestamp)+':\n'+
        str(pdflist)
        + '\n \n Here is the full list of PDF status messages:\n\n' + 
        str(fullstatuslist)
    ]
    yag.send(to, 'PDFs not locked on production: '+str(today), contents)   

# Define input file and file handle for the loop below
inputfile = 'IDs.txt'
idlist = open(inputfile)

# Create empty lists to store status messages for the email notification
stmsgs = []
unlocked = []

# Looks up each printinfo URL and collects status info. If any of the 
# statuses are anything other than "locked", it will send an email notification 
# with a list of unlocked PDFs, as well as the full list of status messages 
# for every collection in the input file.
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
    stmsgs.append(statusmsg)

    if status != "locked":
        unlocked.append(collID)

print "Number of unlocked PDFs: "+str(len(unlocked))+". Sending email to "+ str(', '.join(to)) + "..."

if len(unlocked) > 0:
    ymail()