"""
Get the book id for cnx-archive-export_epub:
- Open cte-cnx-dev.cnx.org
- Navigate to the book
- Expand "more info" tab at the bottom.
- Copy the id for use in the next step
"""

from selenium import webdriver
import os


# Mac OS X only
def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| pbcopy'
    os.system(command)


book = ''
while not book:
    book = raw_input("Enter the number of the book: \n \
        1 - Intro to Soc 2e \n \
        2 - College Physics \n : ")

    if book == '1':
        book = "Introduction to Sociology 2e"
        print "Soc 2e selected, launching browser..."
    elif book == '2':
        book = "College Physics"
        print "College Physics selected, launching browser..."
    else:
        print "invalid input, try again"
        book = False

# adding FF profile removes the 'NoneType' object has no attribute 'path' error when quitting driver
profile = webdriver.FirefoxProfile()

# requires geckodriver: `brew install geckodriver`
driver = webdriver.Firefox(firefox_profile=profile)

driver.get("http://cte-cnx-dev.cnx.org/")
driver.implicitly_wait(30)

link = driver.find_element_by_partial_link_text(book)
link.click()

# find the More Info tab, click on it
driver.implicitly_wait(30)
moreinfo = driver.find_element_by_id('metadata-tab')
moreinfo.click()

# find the cnx book id
idpath = driver.find_element_by_xpath("//dl[@class='dl-horizontal']/dd[2]")
bookid = idpath.text

addToClipBoard(bookid)

print ('Your book ID for %s is %s. It has also been copied to your system clipboard (Cmd+V).' % (book, bookid))

driver.quit()
