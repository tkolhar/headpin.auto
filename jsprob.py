#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import random
import string
import time

url = "https://fry.usersys.redhat.com/headpin"
user = "admin"
password = "admin"


def random_string():
   chars = string.ascii_letters + string.digits
   return "".join(random.choice(chars) for x in range(random.randint(8, 16)))

#driver = webdriver.Firefox()
browser_name = "firefox"
capabilities = getattr(webdriver.DesiredCapabilities, browser_name.upper())
capabilities['version'] = '8'
capabilities['platform'] = 'LINUX'
print capabilities
selenium_url = "http://localhost:4444/wd/hub"
driver = webdriver.Remote(selenium_url, desired_capabilities = capabilities)

driver.get(url)

user_element = driver.find_element_by_id("username")
user_element.send_keys(user)
password_element = driver.find_element_by_id("password")
password_element.send_keys(password)
driver.find_element_by_name("commit").click()
time.sleep(2)
driver.find_element_by_xpath("//a[.='Systems']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[.='Activation Keys']").click()
time.sleep(2)
driver.find_element_by_id("new").click()
time.sleep(2)
name_field = driver.find_element_by_id("activation_key_name")
name_field.send_keys(random_string())
time.sleep(2)
driver.find_element_by_id("save_key").click()
time.sleep(5)
driver.find_element_by_xpath("//a[.= 'Available Subscriptions']").click()
time.sleep(5)
subs = driver.find_elements_by_css_selector("span.fl.subscription_row input")
sub = subs[random.randint(0, len(subs)-1)]
driver.find_element_by_id(sub.get_attribute('id')).click()
time.sleep(2)
add_button = driver.find_element_by_css_selector("input#subscription_submit_button.submit")
add_button.click()
