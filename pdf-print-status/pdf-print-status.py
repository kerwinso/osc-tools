#!/usr/bin/python
import urllib
import datetime
from bs4 import BeautifulSoup
import yagmail

# List of email recipients must be formatted in a list like this: 
# ['email1@host.com','email2@host.com']
to = ['ks52@rice.edu', 'brw5@rice.edu', 'nyxer@rice.edu']

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
booklist = {
    '11406':'College Physics',
    '11407':'Introduction to Sociology',
    '11448':'Biology',
    '11487':'Concepts of Biology',
    '11496':'Anatomy & Physiology',
    '11562':'Statistics',
    '11613':'Economics',
    '11626':'Macroeconomics',
    '11627':'Microeconomics',
    '11629':'Psychology',
    '11667':'Precalculus',
    '11707':'Concepts of Biology - Spanish',
    '11740':'US History',
    '11756':'Basic Math (Prealgebra)',
    '11758':'Algebra & Trigonometry',
    '11759':'College Algebra',
    '11760':'Chemistry',
    '11762':'Sociology 2e',
    '11844':'AP Physics',
    '11858':'AP Micro Economics',
    '11864':'AP Macro Economics',
    '11963':'Calculus (full)',
    '11964':'Calculus (vol. 1)',
    '11965':'Calculus (vol. 2)',
    '11966':'Calculus (vol. 3)',
    '11994':'University Physics'
    }

# Create empty lists to store status messages for the email notification.
# First list: all status messages. Second list: just the unlocked PDFs.
stmsgs = []
unlocked = []

# Looks up each printinfo URL and collects status info. If any of the 
# statuses are anything other than "locked", it will send an email notification 
# with a list of unlocked PDFs, as well as the full list of status messages 
# for every collection in the input file.

for collID,title in sorted(booklist.items()):
    url = 'http://legacy.cnx.org/content/col'+collID+'/latest/printinfo'
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    for s in soup.find_all('div','status'):
        span = s.find('span','data')
        status = span.string
        timestamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        statusmsg = timestamp + ": Process status for col" + collID + " (" + \
            title + "): " + status
        print (statusmsg)
        stmsgs.append(statusmsg)

    if status != "locked":
        book = collID + " " + title
        unlocked.append(book)

print ("Number of unlocked PDFs: "+str(len(unlocked)))

unlocked.sort()
stmsgs.sort()

if len(unlocked) > 0:
    print ("Sending email to "+ str(', '.join(to)) + "...")
    ymail()
