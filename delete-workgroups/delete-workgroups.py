#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
"""
Delete all workgroups on legacy CNX front-end matching user inputted text.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import subprocess
import sys

while True:
    wg = raw_input('Enter text in names of workgroups to delete: ')
    if wg == "":
        print('Please enter a valid workgroup name.')
        continue
    else:
        break

wgtext = '"' + wg + '"'  # put inside quotes so selenium can read the xpath

print ('OK. Launching web browser to search workgroup names for %s...' % wgtext)
URL = 'http://legacy-textbook-dev.cnx.org/mydashboard/manageworkgroups'
driver = webdriver.Chrome()
driver.execute_script('window.focus()')
driver.set_window_position(720, 0)  # fullscreen:1280|laptop:720
driver.set_window_size(720, 800)  # fullscreen:1280,1000|laptop:720,800
driver.get(URL)

print ('Logging in to %s...' % URL)
login_field = driver.find_element(By.ID, '__ac_name')
password_field = driver.find_element(By.ID, '__ac_password')
submit = driver.find_element(By.NAME, 'submit')

login = os.environ['TEXTBOOK_DEV_USER']
password = os.environ['TEXTBOOK_DEV_PASSWORD']
login_field.send_keys(login)
password_field.send_keys(password)
submit.click()

wait = WebDriverWait(driver, 10)

# return a list of wg names that will be deleted
try:
    print ('Searching for %s...' % wgtext)
    # xpath to name of workgroup
    xpath_name = '//h2/a[contains(text(),' + wgtext + ')]'
    workgroups_to_delete = []
    links = wait.until(
                    EC.presence_of_all_elements_located(
                                (By.XPATH, xpath_name)
                    )
                )
    for l in links:
        wg_to_delete = l.get_attribute('textContent')
        workgroups_to_delete.append(wg_to_delete)

    print('\033[91mThe following workgroups will be deleted:')
    for w in workgroups_to_delete:
        print('\t' + w)

except:
    print('Search term not found, exiting and quitting browser.')
    driver.quit()
    sys.exit()

# confirm delete
while True:
    confirm_cancel = raw_input('\033[95mDelete ALL workgroups listed above?'
                               '\n \033[0m1 - Confirm'
                               '\n 2 - Cancel'
                               '\n: '
                               )
    if confirm_cancel == '1':
        break
    elif confirm_cancel == '2':
        print('Cancelled')
        sys.exit()
    else:
        print('Please enter 1 to confirm or 2 to cancel.')
        continue

print ('Looking for the first Delete Workgroup link...')
# xpath to the delete workgroup link
xpath_deletewg = '//h2/a[contains(text(),' + wgtext + ')]/../following-sibling::div/a[3]'


def delete_workgroup():
    """Search and destroy"""
    name_element = driver.find_element(By.XPATH, xpath_name)
    wgname = name_element.get_attribute('textContent')
    print ('Delete Workgroup link found for "%s". Clicking it...' % wgname)
    link.click()
    print ('Looking for delete button...')
    deletebtn = wait.until(
                        EC.element_to_be_clickable(
                            (By.NAME, 'form.button.delete')
                        )
                    )
    print ('Button found: "' + deletebtn.get_attribute('value') + '." Clicking delete button...')
    deletebtn.click()
    print ('Clicked. Loading confirmation page...')
    wait.until(EC.title_is('Openstax Texbook Dev - Personal Workspace'))
    # looks for confirmation on the page after successfully deleting the workgroup
    delconfirmmsg = wait.until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, 'div.portalMessage')
                        )
                    )
    if delconfirmmsg:
        print('Delete confirmed.')
    print ('Looking for next link...')


try:
    while True:
        link = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, xpath_deletewg)
            )
        )
        delete_workgroup()

except:
    print('No more links found, exiting the program and the browser.')
    driver.quit()

finally:
    del_wg_count = str(len(workgroups_to_delete))
    print('Operation complete. Total number of workgroups deleted: %s' % del_wg_count)
    app = '"Terminal"'
    msg = '"Operation complete. Total number of workgroups deleted: ' + del_wg_count + '"'
    bashCommand = "echo; osascript -e 'tell application "+app+"' -e 'activate' -e 'display alert "+msg+"' -e 'end tell'"
    subprocess.call([bashCommand], shell=True)
