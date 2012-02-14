#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import string
import time

url = "https://fry.usersys.redhat.com/headpin"
user = "admin"
password = "admin"


def random_string():
   chars = string.ascii_letters + string.digits
   return "".join(random.choice(chars) for x in range(random.randint(8, 16)))

driver = webdriver.Firefox()
driver.get(url)

user_element = driver.find_element_by_id("username")
user_element.send_keys(user)
password_element = driver.find_element_by_id("password")
password_element.send_keys(password)
login = driver.find_element_by_name("commit")
login.click()
time.sleep(2)
click_locator = driver.find_element_by_xpath("//a[.='Systems']")
click_locator.click()
time.sleep(2)
click_locator = driver.find_element_by_xpath("//a[.='Activation Keys']")
click_locator.click()
time.sleep(2)
click_locator = driver.find_element_by_id("new")
click_locator.click()
time.sleep(2)
name_field = driver.find_element_by_id("activation_key_name")
name_field.send_keys(random_string())
time.sleep(2)
click_locator = driver.find_element_by_id("save_key")
click_locator.click()
time.sleep(2)

