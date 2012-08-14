#!/usr/bin/env python

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.locators import *
import time

#from pages.page import Page
from pages.base import Base

class Home(Base):

    def __init__(self, mozwebqa, open_url=True):
        ''' Gets page ready for testing '''
        Base.__init__(self, mozwebqa)
        if open_url:
            self.selenium.get(self.base_url)
    
    @property        
    def is_username_field_present(self):
        return self.is_element_present(*username_text_field)
    
    @property
    def is_password_field_present(self):
        return self.is_element_present(*password_text_field)
    
    def login(self, user="admin", password="admin"):
        time.sleep(2)
        self.send_text(user,*username_text_field)
        self.send_text(password, *password_text_field)
        self.click(*login_locator)
        time.sleep(3)