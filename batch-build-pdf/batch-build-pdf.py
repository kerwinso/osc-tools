# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

import requests


validserver = False
validfile = False


def chooseserver():
    global validserver, server, baseURL, servername
    server = raw_input("Enter 1 for Textbook-Dev, 2 for Textbook-QA server, 'q' to quit: ")

    if server.lower() == 'q':
        exit()
    elif server == '':
        validserver = True
        print("Dev server chosen")
        baseURL = 'http://legacy-textbook-dev.cnx.org/content/'
        servername = 'Textbook-Dev'
    elif server == '1':
        validserver = True
        print("Dev server chosen")
        baseURL = 'http://legacy-textbook-dev.cnx.org/content/'
        servername = 'Textbook-Dev'
    elif server == '2':
        validserver = True
        print("QA server chosen")
        baseURL = 'http://legacy-textbook-qa.cnx.org/content/'
        servername = 'Textbook-QA'
    else:
        print("try again, enter 1 or 2")


def choosefile():
    global inputfile
    inputfile = raw_input("Enter the name of your text input file (default is './input.txt'): ")
    if inputfile == '':
        inputfile = 'input.txt'


# call the functions above
while not validserver:
    chooseserver()
choosefile()
while not validfile:
    try:
        buildlist = open(inputfile)
        validfile = True
    except:
        print("Invalid file, try again")
        choosefile()

for each in buildlist:
    collID = each.strip()
    if collID.startswith('col') and len(collID) == 8 and collID[3:].isdigit():
        buildurl = urljoin(baseURL, "{}/latest/enqueue".format(collID))
        print("* " + collID + " enqueued on " + servername)
    elif collID[0:4].isdigit() and len(collID) == 5:
        buildurl = urljoin(baseURL + "/col" + "{}/latest/enqueue".format(collID))
        print("* " + collID + " enqueued on " + servername)
    else:
        print("* Skipped collection " + collID + " due to incorrect formatting")
        continue
    response = requests.get(buildurl)
    # Check for HTTP 200 Ok
    if response.status_code != 200:
        # Print to standard error, when the request was not successful.
        print("* Failed to contact {}".format(buildurl), file=sys.stderr)
