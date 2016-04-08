# -*- coding: utf-8 -*-
"""Commandline utility to batch enqueue pdf builds"""
from __future__ import print_function
import os
import sys
import argparse
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

import requests


# Define the unicode function for python3 compatiblity
if getattr(__builtins__, 'unicode', None) is None:
    def unicode(s):
        return s


VALID_SERVERS = {
    # machine-name: (human-name, base-url)
    'dev': ('Textbook-Dev', 'http://legacy-textbook-dev.cnx.org/content/',),
    'qa': ('Textbook-QA', 'http://legacy-textbook-qa.cnx.org/content/',),
}
DEFAULT_SERVER = VALID_SERVERS['dev']


def main(argv=None):
    """Main commandline interface function"""
    parser = argparse.ArgumentParser(description=__doc__)
    server_lines = ["*{}* for {} (at {})".format(key, name, url)
                    for key, (name, url) in VALID_SERVERS.items()]
    server_help = "{} (default '{}')".format(' '.join(server_lines),
                                             DEFAULT_SERVER)
    parser.add_argument('-s', '--server', type=str,
                        choices=VALID_SERVERS.keys(),
                        default='dev', help=server_help)
    parser.add_argument('file', type=argparse.FileType('r'),
                        help="input file containing one indentifier per line")
    args = parser.parse_args(argv)

    servername, baseURL = VALID_SERVERS[args.server]
    buildlist = args.file
    for line in buildlist:
        collID = line.strip()
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

if __name__ == '__main__':
    main()
