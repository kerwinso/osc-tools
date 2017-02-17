##Overview
This script uses Selenium Webdriver to automate deleting workgroups using a Chrome browser instance on CNX (currently textbook-dev server only). 

1. Takes a search term inputted by the user, and returns a list of workgroups matching that term.
1. Deletes all matching workgroups via the necessary clickthroughs.

**Note**: your [environment variables](http://osxdaily.com/2015/07/28/set-enviornment-variables-mac-os-x/) will need to be set properly.

## Dependencies
Python 2.7

Install Selenium:
`pip install selenium`

Install [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/getting-started):

`brew install chromedriver` or `pip install chromedriver`