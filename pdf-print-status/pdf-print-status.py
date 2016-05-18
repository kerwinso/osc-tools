import urllib
import datetime
from bs4 import BeautifulSoup
import yagmail

# List of email recipients must be formatted in a list like this: 
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

# List of all collectionIDs on production
idlist = [
    '11406', '11407', '11448', '11487', '11707', '11496', '11613', '11626', '11627', 
    '11562', '11667', '11629', '11740', '11760', '11758', '11762', '11756', '11759', 
    '11963', '11964', '11965', '11966', '11844', '11858', '11864', '11994'
    ] 

# Create empty lists to store status messages for the email notification.
# First list: all status messages. Second list: just the unlocked PDFs.
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