## Overview
This script checks the print/process status of all the OS-authored collections on production, and sends an email notification to the CM's if any PDFs do not have a "locked" status. 

The email notification can be scheduled as a "cron job" (actually a launchd job), check the [launchd scheduling wiki page](https://github.com/kerwinso/osc-tools/wiki/Scheduling-pdf-print-status-to-run-in-the-background-%28OS-X%29) for more details.

## Dependencies
[Install Beautiful Soup 4:](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

`pip install beautifulsoup4` or `sudo easy_install beautifulsoup4`

You may also have to [install a parser](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser). This script uses lxml:

`pip install lxml` or `sudo easy_install lxml`


Your environment variables will need to be properly set up, see [this page](http://osxdaily.com/2015/07/28/set-enviornment-variables-mac-os-x/) on how to do so for OS X. You will need to know where your bash profile lives.

## launchd Scheduling 

Check the wiki page: [Scheduling pdf-print-status to run in the background on OS X](https://github.com/kerwinso/osc-tools/wiki/Scheduling-pdf-print-status-to-run-in-the-background-%28OS-X%29).
