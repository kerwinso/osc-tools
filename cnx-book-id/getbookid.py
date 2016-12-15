# -*- coding: utf-8 -*-
"""
Get the book id for cnx-archive-export_epub:
- Open cte-cnx-dev.cnx.org
- Navigate to the book
- Expand "more info" tab at the bottom.
- Copy the id for use in whatever is next.
"""

from selenium import webdriver
import os


# Mac OS X only
def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| pbcopy'
    os.system(command)

books = [
    'Algebra and Trigonometry',
    'American Government',
    'Anatomy & Physiology',
    'Biology',
    'Calculus Volume 1',
    'Calculus Volume 2',
    'Calculus Volume 3',
    'Chemistry',
    'Chemistry: Atoms First',
    'College Algebra',
    'College Physics For AP Courses',
    'College Physics',
    'Concepts of Biology',
    'Introduction to Sociology',
    'Introduction to Sociology 2e',
    'Introductory Statistics',
    'Macroeconomics',
    'Microeconomics',
    'Prealgebra',
    'Precalculus',
    'Principles of Economics',
    'Principles of Macroeconomics for AP Courses',
    'Principles of Microeconomics for AP Courses',
    'Psychology',
    'U.S. History'
         ]

book = ''
while not book:
    book = raw_input("Enter the EXACT name of the book (hit Return for book list):  ")
    book = book.strip()

    if book not in books:
        print('Book not found. Valid book titles are: ')
        for b in books:
            print ('\t%s' % b)
        print ('\n')
        book = False
        continue
    else:
        if 'AP' in book:
            book = book.replace('AP', 'AP®')
        print("Browser launching to search for: '%s'" % book)
        print("(browser will quit itself when finished)")

# requires chromedriver: install homebrew, then `brew install chromedriver`
driver = webdriver.Chrome()

try:
    driver.get("http://cte-cnx-dev.cnx.org/")
    driver.implicitly_wait(30)

    link = driver.find_element_by_link_text(book)
    link.click()

    # find the More Information tab, click on it
    driver.implicitly_wait(30)
    moreinfo = driver.find_element_by_id('metadata-tab')
    print('Located "More Information" tab, attempting to grab ID...')
    moreinfo.click()

    # find the cnx book ID under the book name
    xpath = "//dl[@class='dl-horizontal']/dd[2]/div"

    idpath = driver.find_element_by_xpath(xpath)

    bookid = idpath.text

    print(bookid)

    addToClipBoard(bookid)

    print('Book ID found: ' + bookid + '. It has also been copied to your system clipboard (Cmd+V).')
except:
    raise Exception('Something went wrong. Check your Internet or server connection.')
finally:
    driver.quit()
