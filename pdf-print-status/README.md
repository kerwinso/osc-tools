## Dependencies
[Install Beautiful Soup 4:](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

`pip install beautifulsoup4` or `sudo easy_install beautifulsoup4`

You may also have to [install a parser](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser). This script uses lxml:

`pip install lxml` or `sudo easy_install lxml`

You will also need to install [yagmail](https://github.com/kootenpv/yagmail):

`pip install yagmail` or `sudo easy_install yagmail`

## Yagmail Setup
Yagmail uses the keyring lib to securely save your password on your machine -- not inside the script where anyone can read it. To set this up, and to test if yagmail is working on your machine, you can run *yagtest.py*:

`python yagtest.py`

When executed, it will prompt you for the password for os content qa @ gmail . com, after which you can save it. The program will then send a test email to the address(es) listed in `yag.send()`.

##launchd Scheduling 

Check the wiki page: [Scheduling pdf-print-status to run in the background on OS X](https://github.com/kerwinso/osc-tools/wiki/Scheduling-pdf-print-status-to-run-in-the-background-%28OS-X%29).
