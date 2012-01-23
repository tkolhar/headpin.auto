#!/usr/bin/env python

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from pages.base import Base
from pages.page import Page

class Hello(Base):
    _username_locator = (By.CSS_SELECTOR, "div#username")
    _helptips_enabled_locator = (By.CSS_SELECTOR, "input#helptips_enabled")
    _clear_helptips_button_locator = (By.CSS_SELECTOR, "div#clear_helptips.button")
    _password_field_locator = (By.CSS_SELECTOR, "input#password_field")
    _confirm_password_field_locator = (By.CSS_SELECTOR, "input#confirm_field")
    _save_password_button_locator = (By.CSS_SELECTOR, "div#save_password.verify_password")
    _edit_email_locator = (By.CSS_SELECTOR, "div.edit_panel_element")
    _helptips_enabled = (By.XPATH, "//input[@id='helptips_enabled'][@value='1']")
    _helptips_disabled = (By.XPATH, "//input[@id='helptips_enabled'][@value='0']")
    
    @property
    def is_username_present(self):
        return self.is_element_present(*self._username_locator)
    
    @property
    def is_helptips_enabled_present(self):
        return self.is_element_present(*self._helptips_enabled_locator)
    
    def click_helptips(self):
        self.selenium.find_element(*self._account_controller_locator).click()
    
    @property
    def is_helptips_enabled(self):
        return self.is_element_visible(*self._helptips_enabled)
    
    @property
    def is_helptips_disabled(self):
        return self.is_element_visible(*self._helptips_disabled)
    
    def enable_helptips(self):
        if self._helptips_disabled:
            self.selenium.find_element(*self._helptips_enabled_locator).click()
            
    def disable_helptips(self):
        if self._helptips_enabled:
            self.selenium.find_element(*self._helptips_enabled_locator).click()
    
    def change_password(self, password=None):
        new_password_locator = self.selenium.find_element(*self._password_field_locator)
        new_password_locator.send_keys(password)
        confirm_password_locator = self.selenium.find_element(*self._confirm_password_field_locator)
        confirm_password_locator.send_keys(password)
        self.selenium.find_element(*self._save_password_button_locator).click()
        
    def update_email_addr(self, new_email):
        self.selenium.find_element(*self._edit_email_locator).click()
        new_email_locator = self.selenium.find_element(*self._edit_email_locator)
        new_email_locator.send_keys(new_email)
        
        
        
                
        