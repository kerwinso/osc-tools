## Overview
This script uses Selenium Webdriver to automate deleting workgroups using a Chrome browser instance on legacy CNX (currently textbook-dev server only). This is typically required after a botched content-copy-tool operation.

1. Takes a search term inputted by the user, and returns a list of workgroups matching that term.
1. Automatically deletes all matching workgroups via the necessary clickthroughs.

**Note**: your [environment variables](http://osxdaily.com/2015/07/28/set-enviornment-variables-mac-os-x/) will need to be set properly.

## Dependencies
Python 2.7

#### Install Selenium:

`pip install selenium` or `sudo easy_install selenium `


#### Install Homebrew by following the instructions at [http://brew.sh](http://brew.sh/).


#### Install Chromedriver after installing Homebrew:
`brew install chromedriver`

## Annoyances on OS X
Running Selenium, this dialog may constantly pop up:

`Do you want the application "Python.app" to accept incoming network connections?` 

Alas, this message won't go away even if you click Accept.

To remedy:

1. In Terminal, type `which python` and copy the path returned.
1. `sudo codesign -f -s - [YOUR_PYTHON_PATH]` #adds a signature to calm OS X down

If this doesn’t work, you may first have to [disable SIP if you're running El Capitan](http://stackoverflow.com/questions/34760163/how-to-allow-python-app-to-firewall-on-mac-os-x).
