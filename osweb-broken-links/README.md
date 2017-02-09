##Overview
This script checks the HTTP response codes for every link in the OSWeb `sitemap.xml` file and raises an alert if any links are broken.

## Dependencies
Python 2.7

[Install Beautiful Soup 4:](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

`pip install beautifulsoup4` or `sudo easy_install beautifulsoup4`

You may also have to [install a parser](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser). This script uses lxml:

`pip install lxml` or `sudo easy_install lxml`

