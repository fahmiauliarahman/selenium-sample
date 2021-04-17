#!/usr/bin/python3

# pip3 install selenium
# pip3 install webdriver-manager

# to run this script, type: chmod +x ./py-selenium.py && ./py-selenium.py


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
# available since 2.26.0
from selenium.webdriver.support import expected_conditions as EC

import time

# this sample is using chrome as the browser
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
# always use sleep to wait the page to loaded successfully.
time.sleep(1)
driver.get('http://example.com')
wait = WebDriverWait(driver, 5)

# you can use HTML Name attribute to select the element
elName = driver.find_element_by_name('someHTMLName')
# or you can use HTML Full Xpath attribute to select the element
elXpath = driver.find_element_by_xpath('someFullXpathElement')
elName.send_keys('anyInput', Keys.TAB,
                 'or you can send keys on keyboard like this to interact with the element...', Keys.ENTER)

time.sleep(3)
sampleBtn = driver.find_element_by_xpath('xpathForBtn')
btn_lib.click()  # action click button
