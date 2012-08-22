#!/usr/bin/env python

from selenium.webdriver.common.by import By

"""
Locators for aeolus pages are contained within.
"""
# principle nav by direct URL
# in that case only forms and buttons need locators

# options:
# some_locator_by_id = (By.ID, 'someLocator')
# some_locator_by_css = (By.CSS_SELECTOR, '#someLocator')
# some_locator_by_xpath = (By.XPATH, "//div[@id='someLocator']")
# some_elements_locator = (By.CSS_SELECTOR, 'li .someElementsLocator')

username_text_field = (By.NAME, "login")
password_text_field = (By.ID, "password-input")
login_locator = (By.NAME, "commit")

