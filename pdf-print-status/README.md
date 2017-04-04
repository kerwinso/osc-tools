## Overview
This script checks the print/process status of all the OS-authored collections on production, and sends an email notification to the CM's if any PDFs do not have a "locked" status. 

The email notification can be scheduled as a "cron job" (actually a launchd job), check the [launchd scheduling wiki page](https://github.com/kerwinso/osc-tools/wiki/Scheduling-pdf-print-status-to-run-in-the-background-%28OS-X%29) for more details.

## Dependencies
[Install Beautiful Soup 4:](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

`pip install beautifulsoup4` or `sudo easy_install beautifulsoup4`

You may also have to [install a parser](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser). This script uses lxml:

`pip install lxml` or `sudo easy_install lxml`

Refer to [this wiki page](https://github.com/kerwinso/ost-tools/wiki/Local-machine-setup-for-pdf-print-status) to set up your environment variables and other local machine setup for testing.

## launchd Scheduling 

Check the wiki page: [Scheduling pdf-print-status to run in the background on OS X](https://github.com/kerwinso/osc-tools/wiki/Scheduling-pdf-print-status-to-run-in-the-background-%28OS-X%29).
