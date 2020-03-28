from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pause
import pynput
from pynput.keyboard import Key, Controller
from datetime import datetime

#It is made to be used with an institute gmail (To use with Google Meet)
#You can program what time will join to the meet in the date section

#DATE
#####################YEAR#MONTH#DAY#HOUR#MINUTE###### DO NOT PUT ZERO BEFORE A NUMBER
# pause.until(datetime(2020, 3, 27, 11, 29))

# MAIL & PASSWORD (THE MAIL U WILL USE TO ENTER TO THE MEET)
usernameStr = 'MailHere'
passwordStr = 'PasswordHere'
url_meet = 'https://meet.google.com/MEET_ID_HERE'

browser = webdriver.Chrome()
browser.get(('https://accounts.google.com/ServiceLogin?'
             'service=mail&continue=https://mail.google'
             '.com/mail/#identifier'))

username = browser.find_element_by_id('identifierId')
username.send_keys(usernameStr)

nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()

time.sleep(5)

keyboard = Controller()
#keyboard.type(passwordStr)
password = browser.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
password.send_keys(passwordStr)
#keyboard.type(passwordStr)
signInButton = browser.find_element_by_id('passwordNext')
signInButton.click()

time.sleep(3)

# MEET
browser.get(url_meet)
time.sleep(6)
######################################################################################### ↓↓↓↓↓↓↓↓↓↓↓↓ You have to put here the name of the button in your language, in my case it's in Spanish. :)
browser.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Unirme ahora')]").click()
pause
