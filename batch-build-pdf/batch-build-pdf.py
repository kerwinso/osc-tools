# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

import requests


# Define the unicode function for python3 compatiblity
if getattr(__builtins__, 'unicode', None) is None:
    def unicode(s):
        return s


VALID_SERVERS = [
    # machine-name, human-name, base-url
    ('dev', 'Textbook-Dev', 'http://legacy-textbook-dev.cnx.org/content/',),
    ('qa', 'Textbook-QA', 'http://legacy-textbook-qa.cnx.org/content/',),
]
DEFAULT_SERVER = VALID_SERVERS[0]

validserver = False
validfile = False


def chooseserver():
    server_lines = []
    for i, (name, human_name, base_url) in enumerate(VALID_SERVERS):
        line = "  {} for {} (at {})".format(i+1, human_name, base_url)
        server_lines.append(line)

    question = "Enter\n{}\nor 'q' to quit: ".format('\n'.join(server_lines))

    while True:
        server = unicode(raw_input(question))

        if server.lower() == 'q':
            sys.exit(0)
        elif server == '':
            return DEFAULT_SERVER
        elif server.isnumeric():
            i = int(server)
            try:
                return VALID_SERVERS[i-1]
            except IndexError:
                print("try again...")
        else:
            print("try again...")


def choosefile():
    inputfile = raw_input("Enter the name of your text input file (default is './input.txt'): ")
    if inputfile == '':
        inputfile = 'input.txt'
    return inputfile


# call the functions above
name, servername, baseURL = chooseserver()
inputfile = choosefile()
while not validfile:
    try:
        buildlist = open(inputfile)
        validfile = True
    except:
        print("Invalid file, try again")
        inputfile = choosefile()

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
