from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
#from selenium.webdriver.common.by import By

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

profile = webdriver.FirefoxProfile()  
#adding the profile removes the "'NoneType' object has no 
#attribute 'path'"" error when quitting driver

driver = webdriver.Firefox(firefox_profile=profile)

#driver = webdriver.Firefox() #old driver definition

driver.get("http://cte-cnx-dev.cnx.org/")
driver.implicitly_wait(10) #need to test with explicit wait

link = driver.find_element_by_partial_link_text(book)
link.click()

driver.implicitly_wait(5)
moreinfo = driver.find_element_by_id('metadata-tab')
moreinfo.click()

bookid = driver.find_element_by_xpath("//dl[@class='dl-horizontal']/dd[2]")


print 'Your book ID for %s: %s' % (book, bookid.text) 

'''
try:
	element = WebDriverWait(driver,10).until(
		EC.presence_of_element_located((By.LINK_TEXT,'College Physics'))
		)
finally:
	driver.quit()

elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
'''

'''
# subjects = driver.find_element(By.LINK_TEXT, "Subjects")
subjects = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "About Us"))
    )
subjects.Click();

#driver.FindElement(By.LinkText("Subjects")).Click();
'''

#driver.close()

driver.quit()
