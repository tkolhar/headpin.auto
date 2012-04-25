#!/usr/bin/env python

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#from pages.page import Page
from pages.base import Base

class Home(Base):
    _username_text_field = (By.ID, "username")
    _password_text_field = (By.ID, "password")
    _login = (By.NAME, "commit")

    def __init__(self, mozwebqa, open_url=True):
        ''' Gets page ready for testing '''
        Base.__init__(self, mozwebqa)
        if open_url:
            self.selenium.get(self.base_url)
    
    @property        
    def is_username_field_present(self):
        return self.is_element_present(*self._username_text_field)
    
    @property
    def is_password_field_present(self):
        return self.is_element_present(*self._password_text_field)
    
    def login(self, user="admin", password="admin"):
        username_field = self.selenium.find_element(*self._username_text_field)
        username_field.send_keys(user)
        
        password_field = self.selenium.find_element(*self._password_text_field)
        password_field.send_keys(password)
        
        password_field.send_keys(Keys.RETURN)
            
            