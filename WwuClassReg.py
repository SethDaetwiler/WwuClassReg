#!/usr/bin/env python3

import sys
import os
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

f = open("input.txt", "r")
contents = f.readlines()


# read file for user id input
username = contents[0][10:]
password = contents[1][10:]

#open chrome browser
browser = webdriver.Chrome('./chromedriver')
browser.get('https://websso.wwu.edu/cas/login?service=https://mywestern.wwu.edu/mywestern/Login')

#find and send keys to username input with contents of username
usrInput = browser.find_element_by_id('username')
usrInput.send_keys(username)

#find and send keys to password input with contents of password and submit page
passInput = browser.find_element_by_id('password')
passInput.send_keys(password+Keys.ENTER)

#enter

#registration status
browser.get('https://admin.wwu.edu/pls/wwis/bwskrsta.P_RegsStatusDisp')

# TODO: put in date processing to select appropriate term reletive to date of execution

select = browser.find_element_by_id('term_id')
for option in select.find_elements_by_tag_name('option'):
    if 'Fall 2019' in option.text:
        option.click() # select() in earlier versions of webdriver
        break

#submit term selection
browser.find_element_by_xpath("//input[@value='Submit']").click()

#get regDate
regDate = browser.find_element_by_xpath("//span[contains(.,'If eligible')]").text

#substring regDate for key values
regDate = regDate[37:]
regTime = regDate[-8:]
regDate = regDate[:10]


# nav to crn picker
browser.get('https://admin.wwu.edu/pls/wwis/bwskfreg.P_AltPin')

# in crn picker, loop through input for coresponding crn input
for i in range(1,9):
        crnId = ("crn_id%i" % i)
        crnInput = browser.find_element_by_id(crnId)
        
        crnInput.send_keys(contents[1+i][7:])






