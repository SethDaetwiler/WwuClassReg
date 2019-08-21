#!/usr/bin/env python3

import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# TODO: read file for input
username = 'daetwis@wwu.edu'
password = 'slip-3321'

browser = webdriver.Chrome('./chromedriver')
browser.get('https://websso.wwu.edu/cas/login?service=https://mywestern.wwu.edu/mywestern/Login')

#find and send keys to username input with contents of username
usrInput = browser.find_element_by_id('username')
usrInput.send_keys(username)

#find and send keys to password input with contents of password
passInput = browser.find_element_by_id('password')
passInput.send_keys(password)

#enter
passInput.send_keys(Keys.ENTER)

# #nav to web4U
# browser.get('https://admin.wwu.edu/pls/wwis/twbkwbis.P_GenMenu?name=bmenu.P_MainMnu')

# #select student
# studentBtn = browser.find_element_by_link_text('Student')
# studentBtn.click()

# #select registration
# regBtn = browser.find_element_by_link_text('Registration')
# regBtn.click()

# nav to term selection
browser.get('https://admin.wwu.edu/pls/wwis/bwskfreg.P_AltPin')
# TODO: put in date processing to select appropriate term reletive to date of execution
select = browser.find_element_by_id('term_id')
for option in select.find_elements_by_tag_name('option'):
    if option.text == 'Fall 2019':
        option.click() # select() in earlier versions of webdriver
        break

browser.find_element_by_xpath("//input[@value='Submit']").click()



