#!/usr/bin/env python

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from pages.base import Base
from pages.page import Page
import time

class Hello(Base):
    _username_locator = (By.CSS_SELECTOR, "div#username")
    _helptips_enabled_locator = (By.CSS_SELECTOR, "input#helptips_enabled")
    _clear_helptips_button_locator = (By.CSS_SELECTOR, "div#clear_helptips.button")
    _password_field_locator = (By.CSS_SELECTOR, "input#password_field")
    _confirm_password_field_locator = (By.CSS_SELECTOR, "input#confirm_field")
    _save_password_button_locator = (By.CSS_SELECTOR, "div#save_password.verify_password")
    #_edit_email_locator = (By.CSS_SELECTOR, "div.edit_panel_element")
    _edit_email_locator = (By.XPATH, "//div[@name='user[email]']")
    _edit_email_input_locator = (By.XPATH, "//input[@name='user[email]']")
    _helptips_checkbox_locator = (By.XPATH, "//input[@name='user[helptips_enabled]'][@value='1']")
    
    @property
    def is_username_present(self):
        return self.is_element_present(*self._username_locator)
    
    @property
    def is_helptips_enabled_present(self):
        WebDriverWait(self.selenium, 120).until(lambda s: self.is_element_visible(*self._username_locator))
        return self.is_element_present(*self._helptips_enabled_locator)
    
    def click_helptips(self):
        self.selenium.find_element(*self._helptips_checkbox_locator).click()
    
    @property
    def is_helptips_enabled(self):
        WebDriverWait(self.selenium, 60).until(lambda s: self.is_element_visible(*self._helptips_checkbox_locator))
        return self.selenium.find_element(*self._helptips_checkbox_locator).is_selected()
            
    def change_password(self, password=None):
        new_password_locator = self.selenium.find_element(*self._password_field_locator)
        new_password_locator.send_keys(password)
        confirm_password_locator = self.selenium.find_element(*self._confirm_password_field_locator)
        confirm_password_locator.send_keys(password)
        self.selenium.find_element(*self._save_password_button_locator).click()
        
    def update_email_addr(self, new_email):
        WebDriverWait(self.selenium, 120).until(lambda s: self.is_element_visible(*self._username_locator))
        self.selenium.find_element(*self._edit_email_locator).click()
        
        email_input_locator = self.selenium.find_element(*self._edit_email_input_locator)
        email_input_locator.clear()
        email_input_locator.send_keys(new_email+"\n")
        
        
        
                
        